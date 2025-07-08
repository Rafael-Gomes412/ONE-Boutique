document.addEventListener('DOMContentLoaded', () => {
    const mobileMenu = document.querySelector('.mobile-menu');
    const nav = document.querySelector('nav');
    const navLinks = document.querySelectorAll('.navbar a');
    
    // Toggle mobile menu avec pointerdown pour meilleure compatibilité mobile
    mobileMenu.addEventListener('pointerdown', (event) => {
        // Vérifier et utiliser setPointerCapture si disponible
        if (typeof event.target.setPointerCapture === 'function') {
            event.target.setPointerCapture(event.pointerId);
        }
        
        mobileMenu.classList.toggle('active');
        nav.classList.toggle('active');
        
        // Empêcher la propagation pour éviter des fermetures involontaires
        event.stopPropagation();
    });
    
    // Fermer le menu quand on clique sur un lien
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.remove('active');
            nav.classList.remove('active');
        });
    });
    
    // Fermer le menu quand on clique en dehors
    document.addEventListener('click', (event) => {
        const isClickInsideNav = nav.contains(event.target);
        const isClickOnMobileMenu = mobileMenu.contains(event.target);
        
        if (!isClickInsideNav && !isClickOnMobileMenu && nav.classList.contains('active')) {
            mobileMenu.classList.remove('active');
            nav.classList.remove('active');
        }
    });
});