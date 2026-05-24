/* Lost Hills Online -- citynet03 client behaviors
 * EACS v1.1 -- Emergency Archive Continuity System
 */
(function () {

  var pad = function (n) { return n < 10 ? '0' + n : '' + n; };
  var now = new Date();
  var stamp = '[citynet03 ' + pad(now.getHours()) + ':' + pad(now.getMinutes()) + ':' + pad(now.getSeconds()) + ']';
  var bg   = 'background:#1a2436;color:#d8d0a8;padding:2px 6px;font-family:monospace';
  var warn = 'background:#5a2424;color:#f4d8c8;padding:2px 6px;font-family:monospace';
  var dim  = 'color:#5a6a4a;font-family:monospace';

  console.log('%c' + stamp + ' EACS v1.1 initialising -- Shadewater Applied Systems', bg);
  console.log('%c' + stamp + ' citynet03 mirror resuming broadcast', bg);
  console.log('%c' + stamp + ' archive volume B12 mounted (degraded, 17.2 GB on 1.6 GB tape)', bg);
  console.log('%c' + stamp + ' last checkpoint: 05.22.1993  03:17:04 PDT', warn);
  console.log('%c' + stamp + ' auto-restore: checksum FAIL -- restored anyway', warn);

  if (location.pathname.indexOf('/restricted/') >= 0) {
    console.log('%c' + stamp + ' WARNING: /restricted/ accessed from public network', warn);
    console.log('%c' + stamp + ' clerk removal flag: SET; backup process: ignoring', warn);
  } else {
    console.log('%c' + stamp + ' clerk removal queue: ' + (3 + Math.floor(Math.random() * 5)) + ' pending', bg);
  }

  console.log('%c' + stamp + ' field contact: re-established -- source not on personnel list', dim);
  console.log('%c' + stamp + ' [ MAY21_FINAL_DEMO ] suppressed', warn);

  // Page-specific console breadcrumbs
  var path = location.pathname;
  if (path.indexOf('shadewater') >= 0) {
    console.log('%c' + stamp + ' NOTE: shadewater_staff_directory_1993.html removed 05/20/1993 at 03:17', warn);
    console.log('%c' + stamp + ' NOTE: Signal Research division not in public index -- access restricted', warn);
  }
  if (path.indexOf('catfish') >= 0) {
    console.log('%c' + stamp + ' NOTE: depth probe session data archived to B12/sector-317', warn);
    console.log('%c' + stamp + ' NOTE: south pier temperature anomaly -- cause not identified', warn);
  }
  if (path.indexOf('sezzler') >= 0) {
    console.log('%c' + stamp + ' NOTE: B12 referenced in elevator firmware; not on floor plan', warn);
    console.log('%c' + stamp + ' NOTE: guest registry 05/21 -- 41 calls logged between 03:17 and 03:18', warn);
  }
  if (path.indexOf('conference') >= 0) {
    console.log('%c' + stamp + ' NOTE: horizon_mapping_log_052193.txt -- restored, flagged, not removed', warn);
    console.log('%c' + stamp + ' NOTE: Pavilion B12 exhibitor listing withdrawn; has been restored', warn);
  }
  if (path.indexOf('contact') >= 0) {
    console.log('%c' + stamp + ' NOTE: clerk removal queue not processing -- 14 entries held', warn);
    console.log('%c' + stamp + ' NOTE: /cgi-bin/clerk_request.cgi -- last response 05/22/1993 03:17', dim);
  }
  if (path.indexOf('horizon_mapping') >= 0) {
    console.log('%cyou should not be here', 'color:#aa3030;font-family:monospace;font-size:14px;font-weight:bold;');
  }

  // EACS dormancy calculator
  var LAST_ACTIVE = new Date('1993-05-22T03:17:04');
  function calcDormancy() {
    var d     = new Date();
    var msOff = d - LAST_ACTIVE;
    var days  = Math.floor(msOff / (1000 * 60 * 60 * 24));
    var years = Math.floor(days / 365.25);
    var rem   = Math.floor(days - years * 365.25);
    return {
      days:     days,
      years:    years,
      remDays:  rem,
      label:    years + ' years, ' + rem + ' days (' + days.toLocaleString() + ' days total)',
      reconnect: d.toLocaleDateString('en-CA', { year: 'numeric', month: '2-digit', day: '2-digit' })
    };
  }

  // Sitewide EACS status bar
  document.addEventListener('DOMContentLoaded', function () {
    var dom   = calcDormancy();
    var shell = document.querySelector('.shell');
    if (!shell) return;
    var bar = document.createElement('div');
    bar.id  = 'eacs-bar';
    bar.innerHTML =
      '[EACS v1.1] &nbsp;&nbsp;' +
      'EMERGENCY ARCHIVE CONTINUITY &nbsp;&bull;&nbsp; ' +
      'DORMANT ' + dom.years + 'y ' + dom.remDays + 'd &nbsp;&bull;&nbsp; ' +
      'RECONNECTED VIA FIELD TERMINAL &nbsp;&bull;&nbsp; ' +
      'SOURCE NOT ON PERSONNEL LIST &nbsp;&bull;&nbsp; ' +
      'VOLUME B12 DEGRADED';
    shell.insertBefore(bar, shell.firstChild);
    var st = document.createElement('style');
    st.textContent = '#eacs-bar{background:#0e1408;color:#4a6a3a;font-family:"Courier New",monospace;font-size:9px;padding:3px 12px;letter-spacing:0.04em;text-align:center;border-bottom:1px solid #1e2e16;white-space:nowrap;overflow:hidden;}';
    document.head.appendChild(st);
  });

  // EACS panel: dynamic dormancy (index.html)
  document.addEventListener('DOMContentLoaded', function () {
    var dom = calcDormancy();
    var dEl = document.getElementById('eacs-dormancy');
    var rEl = document.getElementById('eacs-reconnect');
    if (dEl) dEl.textContent = dom.label;
    if (rEl) rEl.textContent = dom.reconnect + ' -- connection active';
  });

  // Visitor counter
  document.addEventListener('DOMContentLoaded', function () {
    var counters = document.querySelectorAll('.counter');
    if (!counters.length) return;
    var key = 'citynet_visits';
    var v = parseInt(localStorage.getItem(key) || '317', 10);
    if (isNaN(v)) v = 317;
    v += 1;
    try { localStorage.setItem(key, String(v)); } catch (e) {}
    var s = ('000000' + v).slice(-6);
    counters.forEach(function (c) {
      c.innerHTML = '';
      for (var i = 0; i < s.length; i++) {
        var sp = document.createElement('span');
        sp.textContent = s.charAt(i);
        c.appendChild(sp);
      }
    });
  });

  // Footer timestamps
  document.addEventListener('DOMContentLoaded', function () {
    var dates = ['?? / ?? / 199?', '?? / ?? / 199?', '05 / 22 / 1993', '?? / ?? / 199?', '?? / ?? / 199?'];
    var pick  = dates[Math.floor(Math.random() * dates.length)];
    document.querySelectorAll('.footer .col').forEach(function (el) {
      el.innerHTML = el.innerHTML.replace(/last updated: \?\? \/ \?\? \/ 199\?/, 'last updated: ' + pick);
    });
  });

  // EACS boot sequence (homepage only, once per session)
  document.addEventListener('DOMContentLoaded', function () {
    if (!document.getElementById('eacs-boot-trigger')) return;
    if (sessionStorage.getItem('eacs_boot_done')) return;
    sessionStorage.setItem('eacs_boot_done', '1');

    var dom = calcDormancy();

    var st = document.createElement('style');
    st.textContent = [
      '#eacs-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:#020b02;z-index:9999;display:flex;align-items:center;justify-content:center;opacity:1;transition:opacity 1.4s ease;}',
      '#eacs-terminal{width:600px;max-width:92vw;font-family:"Courier New",monospace;font-size:12px;line-height:1.8;color:#5aaa5a;}',
      '#eacs-terminal .dim{color:#1e3a1e;}',
      '#eacs-terminal .warn{color:#b87828;}',
      '#eacs-terminal .err{color:#aa3030;}',
      '#eacs-terminal .hl{color:#aad4aa;}',
      '#eacs-terminal .brt{color:#ddf0dd;}',
      '.eacs-cur{display:inline-block;animation:eacs-blink .7s step-end infinite;}',
      '@keyframes eacs-blink{0%,100%{opacity:1}50%{opacity:0}}'
    ].join('');
    document.head.appendChild(st);

    var overlay  = document.createElement('div');
    overlay.id   = 'eacs-overlay';
    var terminal = document.createElement('div');
    terminal.id  = 'eacs-terminal';
    overlay.appendChild(terminal);
    document.body.appendChild(overlay);

    var HR = '--------------------------------------------------';
    function row(label, value, cls) {
      var dots = '..................................'.slice(0, Math.max(4, 36 - label.length));
      return { c: cls || '', t: label + ' ' + dots + ' ' + value };
    }

    var lines = [
      { c: 'dim', t: HR },
      { c: 'brt', t: 'SHADEWATER APPLIED SYSTEMS' },
      { c: 'hl',  t: 'EACS v1.1  --  EMERGENCY ARCHIVE CONTINUITY SYSTEM' },
      { c: '',    t: 'Lost Hills Municipal Network  --  node: citynet03' },
      { c: 'dim', t: HR, pause: 200 },
      { c: '',    t: '' },
      row('POWER RESTORE',            'OK'),
      row('CHECKING TAPE VOLUME B12', 'DEGRADED'),
      row('ARCHIVE INDEX',            'PARTIAL RESTORE'),
      row('NETWORK PROBE',            'CONTACT DETECTED'),
      row('SOURCE VERIFICATION',      'NOT ON PERSONNEL LIST',    'warn'),
      row('CLERK REMOVAL FLAG',       'SET -- IGNORED BY BACKUP', 'err'),
      { c: '',    t: '', pause: 300 },
      { c: 'warn',t: 'LAST CHECKPOINT: 05.22.1993  03:17:04 PDT', pause: 180 },
      { c: 'warn',t: 'DAYS IN STANDBY: ' + dom.days.toLocaleString() + '  (' + dom.years + ' years)', pause: 300 },
      { c: '',    t: '' },
      { c: 'err', t: '[ MAY21_FINAL_DEMO ] ................... SUPPRESSED', pause: 200 },
      { c: '',    t: '' },
      { c: 'brt', t: 'RESUMING BROADCAST ............... OPENING ARCHIVE' },
      { c: 'dim', t: HR }
    ];

    var idx  = 0;
    var BASE = 220;

    function addLine() {
      if (idx >= lines.length) {
        var cur = document.createElement('span');
        cur.className   = 'eacs-cur';
        cur.textContent = '_';
        terminal.appendChild(cur);
        setTimeout(function () {
          overlay.style.opacity = '0';
          setTimeout(function () {
            if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
          }, 1500);
        }, 4200);
        return;
      }
      var line = lines[idx];
      var div  = document.createElement('div');
      if (line.c) div.className = line.c;
      div.textContent = line.t;
      terminal.appendChild(div);
      overlay.scrollTop = overlay.scrollHeight;
      idx++;
      setTimeout(addLine, BASE + (line.pause || 0));
    }

    setTimeout(addLine, 400);
  });

})();
