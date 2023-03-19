var prevScrollpos = window.pageYOffset;

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector("header").style.transform = "translateY(0)";
  } else {
    if (currentScrollPos > 100) {
        document.querySelector("header").style.transform = "translateY(-100%)";
    }
  }
  prevScrollpos = currentScrollPos;
}

var alertEl = document.querySelector('.alert-danger');

function showAlert() {
  alertEl.classList.add('show', 'split');
}

function hideAlert() {
  alertEl.classList.remove('show');
}

setTimeout(hideAlert, 5000);


$(document).ready(function(){
  $('.carousel').slick({
    autoplay: true,
    autoplaySpeed: 3000,
    slidesToShow: 3,
    slidesToScroll: 1,
    dots: true,
    infinite: true,
    responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1
          }
        }
      ]
  });
});
