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

  // Price estimate + clear email subject for the owner
  if (main && main.dataset.rates) {
    var R = JSON.parse(main.dataset.rates);
    var fr = main.dataset.lang === 'fr';
    var out = document.getElementById('estimate');
    var fmt = function (n) {
      return fr ? n.toLocaleString('fr-FR') + ' €' : '€' + n.toLocaleString('en-US');
    };
    var md = function (d) { return ('0' + (d.getUTCMonth() + 1)).slice(-2) + '-' + ('0' + d.getUTCDate()).slice(-2); };
    var season = function (d) {
      var k = md(d), from = R.holidayFrom, to = R.holidayTo;
      if (k >= from || k <= to) return 'holiday';
      var m = d.getUTCMonth() + 1;
      return (m === 12 || m <= 4) ? 'high' : 'low';
    };
    var shortDate = function (v) { var p = v.split('-'); return p[2] + '/' + p[1] + '/' + p[0]; };
    var setField = function (n, v) { var el = main.querySelector('[name="' + n + '"]'); if (el) el.value = v; };

    var update = function () {
      var a = q(main, 'checkin').value, b = q(main, 'checkout').value, g = q(main, 'guests').value;
      var name = (document.getElementById('name') || {}).value || '';
      var subject = 'Demande villa';
      if (a && b) subject += ' : ' + shortDate(a) + ' au ' + shortDate(b);
      subject += ', ' + g + ' voyageur' + (g > 1 ? 's' : '');
      if (name) subject += ', ' + name;
      setField('subject', subject);

      if (!a || !b || b <= a) { out.textContent = ''; setField('Nuits', ''); setField('Estimation', ''); return; }
      var d = new Date(a + 'T00:00:00Z'), end = new Date(b + 'T00:00:00Z');
      var nights = 0, total = 0, minNeeded = 0;
      while (d < end) {
        var s = season(d);
        total += R[s][0]; minNeeded = Math.max(minNeeded, R[s][1]);
        nights++; d.setUTCDate(d.getUTCDate() + 1);
      }
      var grand = total + R.cleaning;
      var html = fr
        ? 'Estimation pour ' + nights + ' nuit' + (nights > 1 ? 's' : '') + ' : <strong>' + fmt(grand) + '</strong> (dont ' + fmt(R.cleaning) + ' de ménage), hors taxe de séjour.'
        : 'Estimate for ' + nights + ' night' + (nights > 1 ? 's' : '') + ': <strong>' + fmt(grand) + '</strong> (including ' + fmt(R.cleaning) + ' cleaning), excluding tourist tax.';
      if (nights < minNeeded) {
        html += '<span class="warn">' + (fr
          ? 'Le séjour minimum pour ces dates est de ' + minNeeded + ' nuits.'
          : 'The minimum stay for these dates is ' + minNeeded + ' nights.') + '</span>';
      }
      out.innerHTML = html;
      setField('Nuits', nights + (nights < minNeeded ? ' (minimum ' + minNeeded + ' pour ces dates)' : ''));
      setField('Estimation', total.toLocaleString('fr-FR') + ' € + ' + R.cleaning + ' € ménage = ' + grand.toLocaleString('fr-FR') + ' €');
    };
    ['change', 'input'].forEach(function (ev) { main.addEventListener(ev, update); });
    update();
  }

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
