# Lost Hills Online - GitHub deploy script
#
# ===================== RETIRED 2026-07-25 - DO NOT USE =====================
#
# Deploy with git instead:
#     git add -A && git commit -m "Deploy: <what changed>" && git push
#
# Vercel builds from the repo either way, so a normal push publishes the site.
#
# Why this was retired:
#
#   1. It uploaded truncated files. robots.txt, styles.css and sitemap.xml all
#      ended mid-token in the repo ("Disallow: /restric", "object-positi") while
#      the local copies were complete. Three files cut short at the end is an
#      upload bug in this script, not three coincidences, and it shipped a broken
#      stylesheet to the live site.
#
#   2. It required a GitHub PAT stored in plaintext at
#      uploads/.github_token_losthills.txt, inside the folder of a public site.
#      That token was revoked and the file deleted on 2026-07-25, so read_token()
#      now exits 1 regardless.
#
#   3. It bypassed local git entirely, committing straight through the API. That
#      is why this repo's .git sat broken and unnoticed for months while the
#      remote accumulated 27 deploy commits, and why local and remote could drift
#      without either side showing it.
#
# Kept in the tree for reference only. Delete once nothing references it.
#
# ===========================================================================

import os, json, base64, hashlib, urllib.request, urllib.error, sys, time, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.exit(
    "deploy.py is RETIRED (2026-07-25). Deploy with git instead:\n"
    '  git add -A && git commit -m "Deploy: <what changed>" && git push\n'
    "Vercel builds from the repo. See the header comment for why."
)

REPO       = "BrinShadewater/Lost-Hills-Web"
BRANCH     = "main"
API        = "https://api.github.com"
TOKEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads", ".github_token_losthills.txt")

SKIP = {
    "deploy.py", "uploads", ".git", ".gitignore",
    "FULL-AUDIT-REPORT.md", "ACTION-PLAN.md",
    "assets/README.txt", "assets/Lost Hills Faded", "assets/_unused",
    "assets/sasc-expo.png", "assets/sasc-floorplan.png", "__pycache__",
    "assets/MOFA.png", "assets/SASC.png",
    "assets/Shadewater Labs - website pic.png", "assets/city_seal_lg.png",
}

def read_token():
    if not os.path.exists(TOKEN_FILE):
        print(f"ERROR: Token file not found at {TOKEN_FILE}"); sys.exit(1)
    tok = open(TOKEN_FILE).read().strip()
    if not tok:
        print("ERROR: Token file is empty."); sys.exit(1)
    return tok

def api(method, path, token, body=None):
    url  = f"{API}{path}"
    data = json.dumps(body).encode() if body else None
    req  = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "lost-hills-deploy/1.0")
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} {method} {path}: {e.read().decode()[:200]}")
        raise

def git_hash(path):
    data   = open(path, "rb").read()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()

def has_webp(full):
    base, ext = os.path.splitext(full)
    if ext.lower() not in (".jpg", ".jpeg", ".png"): return False
    return os.path.exists(base + ".webp") or os.path.exists(base.replace("_", "-") + ".webp")

def collect_files(root):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP and not d.startswith(".")]
        for fname in filenames:
            if fname.startswith("."): continue
            full = os.path.join(dirpath, fname)
            rel  = os.path.relpath(full, root).replace("\\", "/")
            if any(rel == s or rel.startswith(s + "/") for s in SKIP): continue
            if rel.startswith("assets/") and has_webp(full): continue
            files.append((rel, full))
    return files

def file_to_blob(path, token, retries=5):
    content = base64.b64encode(open(path, "rb").read()).decode()
    for attempt in range(retries):
        try:
            return api("POST", f"/repos/{REPO}/git/blobs", token,
                       {"content": content, "encoding": "base64"})["sha"]
        except urllib.error.HTTPError as e:
            if e.code == 403 and attempt < retries - 1:
                wait = 15 * (2 ** attempt)
                print(f"  [rate limit] backing off {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise

def get_branch_sha(token):
    try:
        return api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}", token)["object"]["sha"]
    except urllib.error.HTTPError as e:
        if e.code in (404, 409): return None
        raise

def get_remote_tree(commit_sha, token):
    commit   = api("GET", f"/repos/{REPO}/git/commits/{commit_sha}", token)
    tree_sha = commit["tree"]["sha"]
    tree     = api("GET", f"/repos/{REPO}/git/trees/{tree_sha}?recursive=1", token)
    return {i["path"]: i["sha"] for i in tree.get("tree", []) if i["type"] == "blob"}

def push(token):
    root = os.path.dirname(os.path.abspath(__file__))
    print(f"Collecting files from: {root}", flush=True)
    files = collect_files(root)
    print(f"Found {len(files)} files total\n", flush=True)

    commit_sha = get_branch_sha(token)
    if commit_sha is None:
        rel, full = files[0]
        content   = base64.b64encode(open(full, "rb").read()).decode()
        api("PUT", f"/repos/{REPO}/contents/{rel}", token,
            {"message": "Initialize repository", "content": content})
        commit_sha = get_branch_sha(token)

    print("Fetching remote tree to detect changes...", flush=True)
    remote = get_remote_tree(commit_sha, token)
    print(f"Remote has {len(remote)} files\n", flush=True)

    to_upload, tree_entries = [], []
    for rel, full in files:
        lsha = git_hash(full)
        if remote.get(rel) == lsha:
            tree_entries.append({"path": rel, "mode": "100644", "type": "blob", "sha": lsha})
        else:
            to_upload.append((rel, full))

    print(f"Unchanged : {len(tree_entries)} (reusing blobs)", flush=True)
    print(f"New/changed: {len(to_upload)} (uploading)", flush=True)

    if not to_upload:
        print("\nNothing to upload - already up to date.", flush=True); return

    print(f"\nUploading {len(to_upload)} files...", flush=True)
    lock, done = threading.Lock(), [0]

    def upload_one(args):
        rel, full = args
        sha = file_to_blob(full, token)
        with lock:
            done[0] += 1
            print(f"  [{done[0]}/{len(to_upload)}] {rel}", flush=True)
        return rel, sha

    with ThreadPoolExecutor(max_workers=3) as ex:
        for fut in as_completed({ex.submit(upload_one, f): f for f in to_upload}):
            rel, sha = fut.result()
            tree_entries.append({"path": rel, "mode": "100644", "type": "blob", "sha": sha})

    print("\nCreating tree...", flush=True)
    tree = api("POST", f"/repos/{REPO}/git/trees", token, {"tree": tree_entries})

    print("Creating commit...", flush=True)
    commit = api("POST", f"/repos/{REPO}/git/commits", token, {
        "message": "Deploy: Lost Hills Online update",
        "tree": tree["sha"], "parents": [commit_sha],
    })

    print(f"Updating branch {BRANCH}...", flush=True)
    api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", token,
        {"sha": commit["sha"], "force": True})

    print(f"\nDone! Commit: {commit['sha'][:8]}", flush=True)
    print("Vercel will deploy automatically from GitHub.", flush=True)
    print("Live at: https://losthills.net", flush=True)

if __name__ == "__main__":
    push(read_token())
