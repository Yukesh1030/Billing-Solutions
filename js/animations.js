document.addEventListener('DOMContentLoaded', () => {
    // Initialize AOS
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 100
        });
    }

    // GSAP Animations
    if (typeof gsap !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Logo Reveal Animation (Global)
        gsap.from('.nav-brand', {
            opacity: 0,
            y: -20,
            duration: 1,
            ease: 'power3.out'
        });

        gsap.from('.nav-links li', {
            opacity: 0,
            y: -20,
            duration: 0.8,
            stagger: 0.1,
            ease: 'power3.out',
            delay: 0.2
        });

        // Hero Sections Animations (Generic)
        const heroTitle = document.querySelector('.hero-title');
        if (heroTitle) {
            // Very simple split text simulation by fading in whole text for now
            gsap.from(heroTitle, {
                opacity: 0,
                y: 50,
                duration: 1.2,
                ease: 'power4.out',
                delay: 0.5
            });
        }

        const heroContent = document.querySelector('.hero-content p');
        if (heroContent) {
            gsap.from(heroContent, {
                opacity: 0,
                y: 30,
                duration: 1,
                ease: 'power3.out',
                delay: 0.8
            });
        }

        const heroBtns = document.querySelector('.hero-btns');
        if (heroBtns) {
            gsap.from(heroBtns, {
                opacity: 0,
                y: 30,
                duration: 1,
                ease: 'power3.out',
                delay: 1
            });
        }

        // Floating elements logic
        const floatingElements = document.querySelectorAll('.float-element');
        floatingElements.forEach(el => {
            gsap.to(el, {
                y: 'random(-20, 20)',
                x: 'random(-10, 10)',
                duration: 'random(3, 5)',
                repeat: -1,
                yoyo: true,
                ease: 'sine.inOut'
            });
        });

        // Counter Animations
        const counters = document.querySelectorAll('.counter-val');
        counters.forEach(counter => {
            let target = parseInt(counter.getAttribute('data-target') || counter.innerText);
            
            ScrollTrigger.create({
                trigger: counter,
                start: "top 85%",
                once: true,
                onEnter: () => {
                    gsap.to(counter, {
                        innerHTML: target,
                        duration: 2,
                        snap: { innerHTML: 1 },
                        ease: "power1.inOut"
                    });
                }
            });
        });
        
        // Auto slider logic (Basic implementation for Success Stories)
        const sliderContainer = document.querySelector('.auto-slider');
        if (sliderContainer) {
            const slides = sliderContainer.querySelectorAll('.slide');
            if(slides.length > 0){
                let currentSlide = 0;
                setInterval(() => {
                    gsap.to(slides[currentSlide], { opacity: 0, x: -50, duration: 0.5, onComplete: () => {
                        slides[currentSlide].style.display = 'none';
                        currentSlide = (currentSlide + 1) % slides.length;
                        slides[currentSlide].style.display = 'block';
                        gsap.fromTo(slides[currentSlide], { opacity: 0, x: 50 }, { opacity: 1, x: 0, duration: 0.5 });
                    }});
                }, 5000);
                
                // Initialize slides
                slides.forEach((slide, index) => {
                    if (index !== 0) slide.style.display = 'none';
                });
            }
        }
    }
});
