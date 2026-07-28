(() => {
  const lb = document.getElementById('lightboxDialog');
  const lbImg = document.getElementById('lightboxImg');
  if (lb && lbImg) {
    document.querySelectorAll('a.doc-cell, .lic-card a.shot').forEach(a => {
      a.addEventListener('click', e => {
        e.preventDefault();
        lbImg.src = a.getAttribute('href');
        lbImg.alt = a.querySelector('img') ? a.querySelector('img').alt : '';
        lb.showModal();
      });
    });
    lb.addEventListener('click', () => lb.close());
  }

  const cta = document.getElementById('ctaDialog');
  if (cta) {
    const sel = cta.querySelector('select');
    document.querySelectorAll('[data-cta]').forEach(btn => {
      btn.addEventListener('click', () => {
        if (sel) sel.value = btn.dataset.tema || '';
        cta.showModal();
      });
    });
    const closeBtn = cta.querySelector('.cta-dialog-close');
    if (closeBtn) closeBtn.addEventListener('click', () => cta.close());
  }
})();
