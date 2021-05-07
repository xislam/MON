$("ul.programm-caption").on("click", "li:not(.active)", function () {
  $(this)
    .addClass("active")
    .siblings()
    .removeClass("active")
    .closest("div.programm-tabs")
    .find("div.programm-content")
    .removeClass("active")
    .eq($(this).index())
    .addClass("active");
});

const burger = document.getElementById("burger");
const root = document.getElementById("root");
const layer = document.getElementById("layer");
burger.addEventListener("click", function () {
  root.classList.toggle("overflow-hidden");
  layer.classList.toggle("active");
});

let development = document.getElementById("development-parallax");
let home = document.getElementById("home-parallax");

window.addEventListener("scroll", function () {
  let value = window.scrollY;
  development.style.marginBottom = value * 0.4 + "px";
  home.style.top = value * 0.5 + "px";
});

function carouselInit() {
  if ($(window).width() < 576) {
    $(".subdivision-carousel").slick("unslick");
  } else {
    $(".subdivision-carousel").slick({
      infinite: true,
      slidesToShow: 4,
      slidesToScroll: 1,
    });
  }
}
carouselInit();
$(document).ready(function (e) {
  carouselInit();
});
$(window).resize(function () {
  carouselInit();
});

$(".authorities-carousel").slick({
  infinite: true,
  slidesToShow: 4,
  slidesToScroll: 1,

  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        slidesToShow: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
        arrows: false,
        dots: true,
      }
    }
  ]
});

Array.from(document.getElementsByClassName("slick-arrow")).map((item) => {
  return (item.textContent = "");
});
