document.addEventListener('DOMContentLoaded', () => {
    // GSAP Entrance Animation
    if (typeof gsap !== 'undefined') {
        gsap.from('.auth-container', {
            opacity: 0,
            y: 30,
            duration: 1,
            ease: 'power3.out'
        });
        
        gsap.from('.auth-form .form-group', {
            opacity: 0,
            x: -20,
            duration: 0.5,
            stagger: 0.1,
            delay: 0.3,
            ease: 'power2.out'
        });

        gsap.from('.auth-btn', {
            opacity: 0,
            scale: 0.9,
            duration: 0.5,
            delay: 0.8,
            ease: 'back.out(1.7)'
        });
    }

    // Login Form Validation & Redirection
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const loginAs = document.getElementById('loginAs').value;
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();
            
            let isValid = true;
            
            if (!email) {
                document.getElementById('email').style.borderColor = 'red';
                isValid = false;
            } else {
                document.getElementById('email').style.borderColor = 'var(--glass-border)';
            }

            if (!password) {
                document.getElementById('password').style.borderColor = 'red';
                isValid = false;
            } else {
                document.getElementById('password').style.borderColor = 'var(--glass-border)';
            }

            if (isValid) {
                // Store the dynamic username
                localStorage.setItem('billing_username', email);

                // Redirect based on role selection
                if (loginAs === 'Admin') {
                    window.location.href = 'AdminDashboard.html';
                } else {
                    window.location.href = 'ClientDashboard.html';
                }
            }
        });
    }

    // Signup Form Validation & Redirection
    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const inputs = signupForm.querySelectorAll('input, select');
            let isValid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = 'red';
                    isValid = false;
                } else {
                    input.style.borderColor = 'var(--glass-border)';
                }
            });

            if (isValid) {
                // On successful signup, redirect to Login
                window.location.href = 'Login.html';
            }
        });
    }
});
