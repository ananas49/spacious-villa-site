(function () {
  function q(scope, role) { return scope.querySelector('[data-role="' + role + '"]'); }
  function iso(d) { return d.toISOString().slice(0, 10); }

  // Dates: no past dates, check-out after check-in
  var today = iso(new Date());
  document.querySelectorAll('input[type="date"]').forEach(function (el) { el.min = today; });
  document.querySelectorAll('form').forEach(function (f) {
    var a = q(f, 'checkin'), b = q(f, 'checkout');
    if (!a || !b) return;
    a.addEventListener('change', function () {
      if (!a.value) return;
      var d = new Date(a.value); d.setDate(d.getDate() + 1);
      b.min = iso(d);
      if (b.value && b.value <= a.value) b.value = '';
    });
  });

  // Quick booking card fills the full enquiry form
  var quick = document.getElementById('quick-book');
  var main = document.getElementById('enquiry');
  if (quick && main) {
    quick.addEventListener('submit', function (e) {
      e.preventDefault();
      ['checkin', 'checkout', 'guests'].forEach(function (r) {
        var s = q(quick, r), t = q(main, r);
        if (s && t && s.value) { t.value = s.value; t.dispatchEvent(new Event('change')); }
      });
      document.getElementById('book').scrollIntoView();
      var first = document.getElementById('name'); if (first) first.focus({ preventScroll: true });
    });
  }

  // Price calculator (itemized, like a booking site) + clear email subject for the owner
  function calc(R, a, b) {
    var md = function (d) { return ('0' + (d.getUTCMonth() + 1)).slice(-2) + '-' + ('0' + d.getUTCDate()).slice(-2); };
    var season = function (d) {
      var k = md(d);
      if (k >= R.holidayFrom || k <= R.holidayTo) return 'holiday';
      var m = d.getUTCMonth() + 1;
      return (m === 12 || m <= 4) ? 'high' : 'low';
    };
    var d = new Date(a + 'T00:00:00Z'), end = new Date(b + 'T00:00:00Z');
    var groups = {}, order = [], nights = 0, sub = 0, minNeeded = 0;
    while (d < end) {
      var s = season(d);
      if (!groups[s]) { groups[s] = 0; order.push(s); }
      groups[s]++; nights++; sub += R[s][0]; minNeeded = Math.max(minNeeded, R[s][1]);
      d.setUTCDate(d.getUTCDate() + 1);
    }
    var disc = (R.weekly && nights >= R.weekly[0]) ? Math.round(sub * R.weekly[1]) : 0;
    return { groups: groups, order: order, nights: nights, sub: sub, disc: disc, total: sub - disc + R.cleaning, minNeeded: minNeeded };
  }

  document.querySelectorAll('form[data-rates]').forEach(function (form) {
    if (!form.dataset.rates) return;
    var R = JSON.parse(form.dataset.rates);
    var fr = form.dataset.lang === 'fr';
    var box = form.querySelector('[data-estimate]');
    var isMain = form.id === 'enquiry';
    var fmt = function (n) { return fr ? n.toLocaleString('fr-FR') + ' €' : '$' + n.toLocaleString('en-US'); };
    var shortDate = function (v) { var p = v.split('-'); return p[2] + '/' + p[1] + '/' + p[0]; };
    var setField = function (n, v) { var el = form.querySelector('[name="' + n + '"]'); if (el) el.value = v; };
    var nightWord = function (n) { return fr ? (n > 1 ? 'nuits' : 'nuit') : (n > 1 ? 'nights' : 'night'); };

    var update = function () {
      var a = q(form, 'checkin').value, b = q(form, 'checkout').value, g = q(form, 'guests').value;
      if (isMain) {
        var name = (document.getElementById('name') || {}).value || '';
        var subject = 'Demande villa';
        if (a && b) subject += ' : ' + shortDate(a) + ' au ' + shortDate(b);
        subject += ', ' + g + ' voyageur' + (g > 1 ? 's' : '');
        if (name) subject += ', ' + name;
        setField('subject', subject);
      }
      if (!a || !b || b <= a) {
        box.innerHTML = '';
        if (isMain) { setField('Nuits', ''); setField('Estimation', ''); }
        return;
      }
      var r = calc(R, a, b);
      var rows = '';
      r.order.forEach(function (s) {
        var n = r.groups[s];
        rows += '<tr><th scope="row">' + n + ' ' + nightWord(n) + ' × ' + fmt(R[s][0]) +
          (r.order.length > 1 ? '<span>' + R.labels[s] + '</span>' : '') +
          '</th><td>' + fmt(n * R[s][0]) + '</td></tr>';
      });
      if (r.disc) {
        var pct = Math.round(R.weekly[1] * 100);
        rows += '<tr class="calc-disc"><th scope="row">' + (fr ? 'Réduction semaine (−' + pct + ' %)' : 'Weekly discount (−' + pct + '%)') + '</th><td>−' + fmt(r.disc) + '</td></tr>';
      }
      rows += '<tr><th scope="row">' + (fr ? 'Ménage' : 'Cleaning fee') + '</th><td>' + fmt(R.cleaning) + '</td></tr>';
      var html = '<table class="calc"><tbody>' + rows + '</tbody><tfoot><tr><th scope="row">Total</th><td>' + fmt(r.total) + '</td></tr></tfoot></table>' +
        '<p class="calc-note">' + (fr ? 'Hors taxe de séjour. Aucuns frais de service.' : 'Excluding tourist tax. No service fees.') + '</p>';
      if (r.nights < r.minNeeded) {
        html += '<p class="warn">' + (fr
          ? 'Le séjour minimum pour ces dates est de ' + r.minNeeded + ' nuits.'
          : 'The minimum stay for these dates is ' + r.minNeeded + ' nights.') + '</p>';
      }
      box.innerHTML = html;
      if (isMain) {
        setField('Nuits', r.nights + (r.nights < r.minNeeded ? ' (minimum ' + r.minNeeded + ' pour ces dates)' : ''));
        setField('Estimation', fmt(r.sub) + (r.disc ? ' − ' + fmt(r.disc) + ' réduction semaine' : '') + ' + ' + fmt(R.cleaning) + ' ménage = ' + fmt(r.total) + (fr ? '' : ' (USD)'));
      }
    };
    ['change', 'input'].forEach(function (ev) { form.addEventListener(ev, update); });
    update();
  });

  // Gallery lightbox
  var lb = document.getElementById('lightbox');
  var items = Array.prototype.slice.call(document.querySelectorAll('.gallery button'));
  if (lb && items.length) {
    var img = lb.querySelector('img'), cap = lb.querySelector('figcaption'), i = 0, last = null;
    function show(n) {
      i = (n + items.length) % items.length;
      var src = items[i].querySelector('img');
      img.src = src.getAttribute('data-full') || src.src; img.alt = src.alt; cap.textContent = src.alt;
    }
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; if (last) last.focus(); }
    items.forEach(function (b, n) {
      b.addEventListener('click', function () { last = b; show(n); lb.classList.add('open'); document.body.style.overflow = 'hidden'; lb.querySelector('.lb-close').focus(); });
    });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(i - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(i + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(i - 1);
      if (e.key === 'ArrowRight') show(i + 1);
    });
  }
})();
