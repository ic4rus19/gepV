let lastScrollTop = 0;

window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar");
    if (!navbar) return;

    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop && scrollTop > 100) {
        navbar.classList.add("nav-hidden");
        navbar.classList.remove("nav-visible");
    } else {
        navbar.classList.add("nav-visible");
        navbar.classList.remove("nav-hidden");
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});

