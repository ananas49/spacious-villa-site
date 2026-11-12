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

  // Quick booking card: fills the enquiry form on the same page, or carries the dates to the booking page
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
    });
  }
  if (main) {
    var params = new URLSearchParams(location.search), filled = false;
    ['checkin', 'checkout', 'guests'].forEach(function (r) {
      var v = params.get(r), t = q(main, r);
      if (v && t && /^[0-9-]{1,10}$/.test(v)) { t.value = v; filled = true; }
    });
    if (filled) { setTimeout(function () { main.dispatchEvent(new Event('change')); main.scrollIntoView(); }, 0); }
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
    var inEl = q(form, 'checkin'), outEl = q(form, 'checkout');
    var nOut = form.querySelector('.sim-n'), minus = form.querySelector('.sim-minus'), plus = form.querySelector('.sim-plus');
    var n = parseInt(form.dataset.nights, 10) || 5, MIN = 1, MAX = 30;
    var fmt = function (v) { return fr ? v.toLocaleString('fr-FR') + ' €' : '$' + v.toLocaleString('en-US'); };
    var shortDate = function (v) { var p = v.split('-'); return p[2] + '/' + p[1] + '/' + p[0]; };
    var setField = function (name, v) { var el = form.querySelector('[name="' + name + '"]'); if (el) el.value = v; };
    var nightWord = function (k) { return fr ? (k > 1 ? 'nuits' : 'nuit') : (k > 1 ? 'nights' : 'night'); };
    var addDays = function (v, k) { var d = new Date(v + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() + k); return iso(d); };
    var between = function (a, b) { return Math.round((new Date(b + 'T00:00:00Z') - new Date(a + 'T00:00:00Z')) / 86400000); };
    var noteHtml = '<p class="calc-note">' + (fr ? 'Hors taxe de séjour. Aucuns frais de service.' : 'Excluding tourist tax. No service fees.') + '</p>';

    var payLine = function (total, checkin) {
      var days = between(today, checkin);
      if (!R.depositPct || days < R.balanceDays) {
        return fr ? 'Séjour dans moins de ' + R.balanceDays + ' jours : totalité due à la réservation.'
                  : 'Stay within ' + R.balanceDays + ' days: full amount due at booking.';
      }
      var dep = Math.round(total * R.depositPct / 100);
      return fr ? 'Acompte de ' + R.depositPct + ' % à la réservation : <strong>' + fmt(dep) + '</strong>. Solde ' + R.balanceDays + ' jours avant l\'arrivée.'
                : R.depositPct + '% deposit at booking: <strong>' + fmt(dep) + '</strong>. Balance due ' + R.balanceDays + ' days before arrival.';
    };

    // No dates yet: total for N nights in each season
    var bySeason = function () {
      var rows = '';
      ['low', 'high', 'holiday'].forEach(function (s) {
        var cell;
        if (n < R[s][1]) {
          cell = '<span class="sim-min">' + (fr ? R[s][1] + ' nuits min.' : R[s][1] + ' nights min.') + '</span>';
        } else {
          var sub = R[s][0] * n, disc = (R.weekly && n >= R.weekly[0]) ? Math.round(sub * R.weekly[1]) : 0;
          cell = fmt(sub - disc + R.cleaning);
        }
        rows += '<tr><th scope="row">' + R.labels[s] + '<span>' + fmt(R[s][0]) + (fr ? ' la nuit' : ' per night') + '</span></th><td>' + cell + '</td></tr>';
      });
      return '<p class="calc-cap">' + (fr ? 'Pour ' + n + ' ' + nightWord(n) + ', ménage compris :' : 'For ' + n + ' ' + nightWord(n) + ', cleaning included:') + '</p>' +
        '<table class="calc calc-seasons"><tbody>' + rows + '</tbody></table>' +
        '<p class="calc-pay">' + (fr ? 'Choisissez vos dates pour le prix exact.' : 'Choose your dates for the exact price.') + '</p>' + noteHtml;
    };

    var update = function () {
      var a = inEl.value, b = outEl.value, g = q(form, 'guests').value;
      if (isMain) {
        var name = (document.getElementById('name') || {}).value || '';
        var subject = 'Demande villa';
        if (a && b) subject += ' : ' + shortDate(a) + ' au ' + shortDate(b);
        subject += ', ' + g + ' voyageur' + (g > 1 ? 's' : '');
        if (name) subject += ', ' + name;
        setField('subject', subject);
      }
      var valid = a && b && b > a;
      if (valid) n = Math.min(MAX, between(a, b));
      if (nOut) { nOut.textContent = n; minus.disabled = n <= MIN; plus.disabled = n >= MAX; }
      if (!valid) {
        box.innerHTML = isMain ? bySeason() : '';
        if (isMain) { setField('Nuits', ''); setField('Estimation', ''); }
        return;
      }
      var r = calc(R, a, b);
      var rows = '';
      r.order.forEach(function (s) {
        var k = r.groups[s];
        rows += '<tr><th scope="row">' + k + ' ' + nightWord(k) + ' × ' + fmt(R[s][0]) +
          (r.order.length > 1 ? '<span>' + R.labels[s] + '</span>' : '') +
          '</th><td>' + fmt(k * R[s][0]) + '</td></tr>';
      });
      if (r.disc) {
        var pct = Math.round(R.weekly[1] * 100);
        rows += '<tr class="calc-disc"><th scope="row">' + (fr ? 'Réduction séjour à la semaine (−' + pct + ' %)' : 'Weekly stay discount (−' + pct + '%)') + '</th><td>−' + fmt(r.disc) + '</td></tr>';
      }
      rows += '<tr><th scope="row">' + (fr ? 'Frais de ménage' : 'Cleaning fee') + '</th><td>' + fmt(R.cleaning) + '</td></tr>';
      var html = '<table class="calc"><tbody>' + rows + '</tbody><tfoot><tr><th scope="row">Total <span class="cur">' + (fr ? 'EUR' : 'USD') + '</span></th><td>' + fmt(r.total) + '</td></tr></tfoot></table>' +
        '<p class="calc-pay">' + payLine(r.total, a) + '</p>' + noteHtml;
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

    // Nights stepper: moves the check-out date when a check-in is set
    var step = function (d) {
      n = Math.max(MIN, Math.min(MAX, n + d));
      if (inEl.value) { outEl.value = addDays(inEl.value, n); }
      else if (outEl.value) { outEl.value = ''; }
      update();
    };
    if (minus) {
      minus.addEventListener('click', function () { step(-1); });
      plus.addEventListener('click', function () { step(1); });
      inEl.addEventListener('change', function () {
        if (inEl.value && !outEl.value) { outEl.value = addDays(inEl.value, n); }
      });
    }
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
