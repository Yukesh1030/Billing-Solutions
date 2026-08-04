document.addEventListener('DOMContentLoaded', () => {
    // Sidebar Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', () => {
            sidebar.classList.toggle('active');
        });
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (sidebar && sidebar.classList.contains('active')) {
            if (!sidebar.contains(e.target) && !menuToggle.contains(e.target)) {
                sidebar.classList.remove('active');
            }
        }
    });

    // Load dynamic username from login
    const dynamicName = localStorage.getItem('billing_username');
    if (dynamicName) {
        const usernameElements = document.querySelectorAll('.user-info h4');
        usernameElements.forEach(el => {
            el.textContent = dynamicName;
        });
        
        // Update avatar letter
        const avatarElements = document.querySelectorAll('.user-profile div:first-child');
        avatarElements.forEach(el => {
            if (el.style.width === '40px') {
                el.textContent = dynamicName.charAt(0).toUpperCase();
            }
        });
    }

    // Logout handler
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = 'Login.html';
        });
    }
    // Form Validation Logic for dashboards (Generic for forms redirecting to 404)
    const genericForms = document.querySelectorAll('form.redirect-404');
    genericForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // Basic validation check
            let isValid = true;
            const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
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
