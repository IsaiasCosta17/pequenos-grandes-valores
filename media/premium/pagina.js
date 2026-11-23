const video = document.querySelector('#video');
let iniciou = false;
let viuMetade = false;

video.addEventListener('play', () => {
  if (iniciou) return;
  iniciou = true;
  window.fbq?.('trackCustom', 'VideoPlay', { content_name: 'VSL 50 Exercicios' });
});

video.addEventListener('timeupdate', () => {
  if (viuMetade || video.currentTime < 93) return;
  viuMetade = true;
  window.fbq?.('trackCustom', 'VideoHalf', { content_name: 'VSL 50 Exercicios' });
});

document.addEventListener('click', (event) => {
  if (!event.target.closest('[data-checkout]')) return;
  window.fbq?.('trackCustom', 'ClicouComprar');
  window.fbq?.('track', 'InitiateCheckout', { value: 29.90, currency: 'BRL' });
});

const visuais = new Map([
  [video, () => { video.poster = video.dataset.poster; }],
  ...Array.from(document.querySelectorAll('.desafios, .escudo'), (elemento) => [
    elemento, () => elemento.classList.add('fotos-prontas'),
  ]),
]);

if ('IntersectionObserver' in window) {
  const observador = new IntersectionObserver((entradas) => {
    for (const entrada of entradas) {
      if (!entrada.isIntersecting) continue;
      visuais.get(entrada.target)();
      observador.unobserve(entrada.target);
    }
  }, { rootMargin: '180px' });
  for (const elemento of visuais.keys()) observador.observe(elemento);
} else {
  for (const carregar of visuais.values()) carregar();
}
