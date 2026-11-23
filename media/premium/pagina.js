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
