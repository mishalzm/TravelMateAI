
// ================================
// DARK MODE
// ================================

const themeButton = document.getElementById("theme-toggle");

let currentTheme = localStorage.getItem("theme") || "light";

document.documentElement.setAttribute("data-theme", currentTheme);

function updateButton() {
    if (!themeButton) return;

    themeButton.textContent =
        currentTheme === "dark" ? "☀️ Light Mode" : "🌙 Dark Mode";
}

updateButton();

if (themeButton) {
    themeButton.addEventListener("click", function () {

        currentTheme =
            currentTheme === "light" ? "dark" : "light";

        document.documentElement.setAttribute("data-theme", currentTheme);

        localStorage.setItem("theme", currentTheme);

        updateButton();
    });
}


// ================================
// DESTINATION SEARCH AND FILTER
// ================================

const searchInput = document.getElementById("destination-search");
const interestFilter = document.getElementById("interest-filter");

function filterDestinations() {

    const searchValue = searchInput
        ? searchInput.value.toLowerCase().trim()
        : "";

    const selectedInterest = interestFilter
        ? interestFilter.value.toLowerCase()
        : "all";

    const cards = document.querySelectorAll(
        ".destination-grid .destination-card"
    );

    cards.forEach(function (card) {

        const nameElement = card.querySelector("h3");
        const categoryElement = card.querySelector(".destination-category");

        const destinationName = nameElement
            ? nameElement.textContent.toLowerCase()
            : "";

        const destinationInterest = categoryElement
            ? categoryElement.textContent.toLowerCase().trim()
            : "";

        const matchesSearch =
            destinationName.includes(searchValue);

        const matchesInterest =
            selectedInterest === "all" ||
            destinationInterest === selectedInterest;

        card.style.display =
            matchesSearch && matchesInterest ? "" : "none";

    });
}

if (searchInput) {
    searchInput.addEventListener("input", filterDestinations);
}

if (interestFilter) {
    interestFilter.addEventListener("change", filterDestinations);
}

