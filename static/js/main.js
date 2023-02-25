// Select all the links in the navbar
const links = document.querySelectorAll("nav a");
// Add event listeners to each link
links.forEach(link => {
    link.addEventListener("click", function (event) {
        // Prevent default link behavior
        event.preventDefault();

        // Get the target element by its ID
        const targetId = this.getAttribute("href");
        const targetElement = document.querySelector(targetId);

        // Get the offset position of the target element
        const offset = 80; // Change this value to adjust the offset
        const targetPosition = targetElement.offsetTop - offset;

        // Animate scrolling to the target element
        window.scrollTo({
            top: targetPosition,
            behavior: "smooth"
        });
    });
});

// smooth scroll behaviour
$(document).ready(function () {
    $('a[href^="#"]').on('click', function (event) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            event.preventDefault();
            $('html, body').animate({
                scrollTop: target.offset().top
            }, 1000);
        }
    });
});
