const menuIcon = document.getElementById('menu-icon');
const overlayMenu = document.getElementById('overlay-menu');
const closeButton = document.getElementById('close-button');

menuIcon.addEventListener('click', () => {
    overlayMenu.classList.add('show');
});

menuIcon.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    overlayMenu.classList.add('show');
  }
});

closeButton.addEventListener('click', () => {
    overlayMenu.classList.remove('show');
});