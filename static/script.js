document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchInput = document.getElementById('search');
    const jobListings = document.querySelectorAll('.job-listing');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value.toLowerCase();
        jobListings.forEach(listing => {
            const title = listing.querySelector('h2').textContent.toLowerCase();
            const company = listing.querySelector('.company').textContent.toLowerCase();
            const location = listing.querySelector('.location').textContent.toLowerCase();
            const description = listing.querySelector('.description').textContent.toLowerCase();

            if (title.includes(query) || company.includes(query) || location.includes(query) || description.includes(query)) {
                listing.style.display = 'block';
            } else {
                listing.style.display = 'none';
            }
        });
    });
});
