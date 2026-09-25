document.addEventListener('DOMContentLoaded', () => {

  // Footer year
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Mobile nav toggle
  const menuToggle = document.getElementById('menu-toggle');
  const mainNav = document.getElementById('main-nav');
  if (menuToggle && mainNav) {
    menuToggle.addEventListener('click', () => {
      const isOpen = mainNav.classList.toggle('mobile-open');
      menuToggle.classList.toggle('open', isOpen);
      menuToggle.setAttribute('aria-expanded', String(isOpen));
    });

    // Dropdown toggle on mobile (tap parent to expand submenu)
    mainNav.querySelectorAll('.has-dropdown > a').forEach(link => {
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 860) {
          const parent = link.parentElement;
          const alreadyOpen = parent.classList.contains('open');
          if (!alreadyOpen) {
            e.preventDefault();
            parent.classList.add('open');
          }
        }
      });
    });

    // Close mobile nav when a normal link is tapped
    mainNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 860 && !link.parentElement.classList.contains('has-dropdown')) {
          mainNav.classList.remove('mobile-open');
          menuToggle.classList.remove('open');
          menuToggle.setAttribute('aria-expanded', 'false');
        }
      });
    });
  }

  // Testimonial dots + scroll sync
  const track = document.getElementById('testimonial-track');
  const dotsWrap = document.getElementById('testimonial-dots');
  if (track && dotsWrap) {
    const cards = Array.from(track.children);
    cards.forEach((_, i) => {
      const dot = document.createElement('span');
      if (i === 0) dot.classList.add('active');
      dot.addEventListener('click', () => {
        cards[i].scrollIntoView({ behavior: 'smooth', inline: 'start', block: 'nearest' });
      });
      dotsWrap.appendChild(dot);
    });
    const dots = Array.from(dotsWrap.children);

    let scrollTimeout;
    track.addEventListener('scroll', () => {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        const trackCenter = track.scrollLeft + track.clientWidth / 2;
        let closest = 0;
        let closestDist = Infinity;
        cards.forEach((card, i) => {
          const cardCenter = card.offsetLeft + card.clientWidth / 2;
          const dist = Math.abs(cardCenter - trackCenter);
          if (dist < closestDist) { closestDist = dist; closest = i; }
        });
        dots.forEach((d, i) => d.classList.toggle('active', i === closest));
      }, 80);
    });
  }

  // Scroll reveal for key sections
  const revealTargets = document.querySelectorAll(
    '.service-card, .feature-row, .about-grid, .article-card, .gallery-item, .section-head, .city-card'
  );
  revealTargets.forEach(el => el.classList.add('reveal'));

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealTargets.forEach(el => observer.observe(el));
  } else {
    revealTargets.forEach(el => el.classList.add('in-view'));
  }

  // Contact form — no backend on a static host, so the enquiry is handed
  // straight to WhatsApp with every field pre-filled.
  const WHATSAPP_NUMBER = '919410770925';
  const form = document.getElementById('contact-form');
  const note = document.getElementById('form-note');
  if (form && note) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const lines = [
        'Namaste Acharya Ji,',
        '',
        'Name: ' + (data.get('name') || '—'),
        'Phone: ' + (data.get('phone') || '—'),
        'Email: ' + (data.get('email') || '—'),
        'City: ' + (data.get('city') || '—'),
        'Ceremony: ' + (data.get('ceremony') || '—'),
        '',
        (data.get('message') || '').trim()
      ];
      const url = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' +
        encodeURIComponent(lines.join('\n').trim());
      window.open(url, '_blank', 'noopener');
      note.textContent = 'Opening WhatsApp with your enquiry — if nothing opens, call +91 94107 70925 directly.';
    });
  }

  // Header shadow on scroll
  const header = document.getElementById('header');
  if (header) {
    window.addEventListener('scroll', () => {
      header.style.boxShadow = window.scrollY > 12 ? '0 8px 30px rgba(0,0,0,0.35)' : 'none';
    });
  }
});
