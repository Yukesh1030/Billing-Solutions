document.addEventListener('DOMContentLoaded', () => {
    // Navbar Sticky and Scroll Effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('sticky');
        } else {
            navbar.classList.remove('sticky');
        }
    });

    // Hamburger Menu Logic
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            
            // Toggle hamburger icon (optional: you can use an icon font or SVG manipulation here)
            if(navLinks.classList.contains('active')){
                hamburger.innerHTML = '&#10005;'; // X mark
            } else {
                hamburger.innerHTML = '&#9776;'; // Hamburger
            }
        });
    }

    // Close mobile menu when a link is clicked
    const links = document.querySelectorAll('.nav-links a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                if(hamburger) hamburger.innerHTML = '&#9776;';
            }
        });
    });

    // Form Validation Logic (Generic for forms redirecting to 404)
    const genericForms = document.querySelectorAll('form.redirect-404');
    genericForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // Basic validation check
            let isValid = true;
            const inputs = form.querySelectorAll('input[required], textarea[required]');
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = 'red';
                } else {
                    input.style.borderColor = 'var(--glass-border)';
                }
            });

            if (isValid) {
                window.location.href = '404.html';
            }
        });
    });
});
