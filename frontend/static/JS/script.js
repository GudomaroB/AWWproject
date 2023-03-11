document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("bur").addEventListener("click", function () {
    document.querySelector("header").classList.toggle("test");
  });
});

document.getElementById("modals").addEventListener("click", function () {
  document.getElementById("my-modal").classList.add("open");
});
document.getElementById("close-my-btn").addEventListener("click", function () {
  document.getElementById("my-modal").classList.remove("open");
});

//!
let acc = document.getElementsByClassName("accordion");
let i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    let panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}
