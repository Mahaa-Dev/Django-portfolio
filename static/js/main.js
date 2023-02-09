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
