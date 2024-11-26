// Portfolio Filter Functionality
function filterPortfolio(category) {
    const items = document.querySelectorAll('.portfolio-item');
    items.forEach(item => {
        if (category === 'all' || item.classList.contains(category)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// AOS (Animate on Scroll) Initialization
AOS.init({
    duration: 1200, // Animation duration
    easing: 'ease-in-out', // Animation easing
    once: true, // Animation triggers only once
    mirror: false, // Do not repeat animations when scrolling back
});

// Sticky Navbar
window.onscroll = function () {
    let navbar = document.querySelector('.navbar');
    if (window.pageYOffset > 100) {
        navbar.classList.add('navbar-sticky');
    } else {
        navbar.classList.remove('navbar-sticky');
    }
};

// Navbar Active State for ScrollSpy
document.addEventListener('scroll', function () {
    let sections = document.querySelectorAll('section');
    let navbarLinks = document.querySelectorAll('.navbar-nav .nav-link');

    sections.forEach(section => {
        if (window.scrollY >= section.offsetTop - 50 && window.scrollY < section.offsetTop + section.offsetHeight) {
            navbarLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + section.id) {
                    link.classList.add('active');
                }
            });
        }
    });
});
