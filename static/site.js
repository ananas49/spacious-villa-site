(function () {
  // Dates: no past dates, check-out after check-in
  var today = new Date().toISOString().slice(0, 10);
  document.querySelectorAll('input[type="date"]').forEach(function (el) { el.min = today; });
  function pair(inName, outName, scope) {
    var a = scope.querySelector('[name="' + inName + '"]'), b = scope.querySelector('[name="' + outName + '"]');
    if (!a || !b) return;
    a.addEventListener('change', function () {
      if (!a.value) return;
      var d = new Date(a.value); d.setDate(d.getDate() + 1);
      b.min = d.toISOString().slice(0, 10);
      if (b.value && b.value <= a.value) b.value = '';
    });
  }
  document.querySelectorAll('form').forEach(function (f) { pair('checkin', 'checkout', f); });

  // Quick booking card fills the full enquiry form
  var quick = document.getElementById('quick-book');
  var main = document.getElementById('enquiry');
  if (quick && main) {
    quick.addEventListener('submit', function (e) {
      e.preventDefault();
      ['checkin', 'checkout', 'guests'].forEach(function (n) {
        var s = quick.querySelector('[name="' + n + '"]'), t = main.querySelector('[name="' + n + '"]');
        if (s && t && s.value) t.value = s.value;
      });
      document.getElementById('book').scrollIntoView();
      var first = main.querySelector('[name="name"]'); if (first) first.focus({ preventScroll: true });
    });
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
