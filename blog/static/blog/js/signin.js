function showForm(formType) {
        const signupForm = document.getElementById('signupForm');
        const signinForm = document.getElementById('signinForm');
        const tabs = document.querySelectorAll('.tab-btn');

        tabs.forEach(tab => tab.classList.remove('active'));

        if (formType === 'signup') {
        signupForm.classList.remove('hidden');
        signinForm.classList.add('hidden');
        tabs[0].classList.add('active');
        } else {
        signinForm.classList.remove('hidden');
        signupForm.classList.add('hidden');
        tabs[1].classList.add('active');
        }
    }