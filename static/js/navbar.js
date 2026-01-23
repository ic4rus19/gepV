let lastScrollTop = 0;
const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", function () {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop && scrollTop > 100) {
        // Bajando → ocultar
        navbar.classList.add("nav-hidden");
        navbar.classList.remove("nav-visible");
    } else {
        // Subiendo → mostrar
        navbar.classList.add("nav-visible");
        navbar.classList.remove("nav-hidden");
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});
