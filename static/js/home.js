const darkBtn = document.getElementById("darkBtn");
const lightBtn = document.getElementById("lightBtn");

darkBtn.addEventListener("click", function () {
    document.body.classList.add("dark-mode");
});

lightBtn.addEventListener("click", function () {
    document.body.classList.remove("dark-mode");
});
