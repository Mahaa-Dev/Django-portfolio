const name = "{{ info.name }}".split(" ");
const title = "{{ info.title }}".split(" ");
let i = 0;
let j = 0;

function displayName() {
    if (i < name.length) {
        document.getElementById("name").innerHTML += name[i] + " ";
        i++;
        setTimeout(displayName, 500);
    }
}

function displayTitle() {
    if (j < title.length) {
        document.getElementById("title").innerHTML += title[j] + " ";
        j++;
        setTimeout(displayTitle, 500);
    }
}


// for off setting the navbar

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

