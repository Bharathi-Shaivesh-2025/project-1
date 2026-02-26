/* ============= CONTACT PAGE SCRIPT ============= */

document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', handleContactSubmission);
    }
});

async function handleContactSubmission(e) {
    e.preventDefault();

    // Collect form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;

    // Validate
    if (!name || !email || !subject || !message) {
        showMessage('formMessage', 'Please fill in all fields', 'error');
        return;
    }

    try {
        // Call API
        const response = await apiCall('/api/contact', 'POST', {
            name: name,
            email: email,
            subject: subject,
            message: message
        });

        if (response.success) {
            showMessage('formMessage', response.message, 'success');
            document.getElementById('contactForm').reset();
        } else {
            throw new Error(response.error || 'Failed to send message');
        }
    } catch (error) {
        console.error('Error:', error);
        showMessage('formMessage', 'Error sending message. Please try again.', 'error');
    }
}
