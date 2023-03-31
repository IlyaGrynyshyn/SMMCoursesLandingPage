// Slider
$(document).ready(function () {
    $('.slider').slick({
        dots: true,
        arrows: false,
        infinite: true,
        speed: 700,
        slidesToShow: 2,
        slidesToScroll: 2,
        responsive: [
            {
                breakpoint: 993,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
        ]
    });
});

$('.slider-prev').on('click', function () {
    $('.slider').slick('slickPrev')
})

$('.slider-next').on('click', function () {
    $('.slider').slick('slickNext')
})

// PopUp
const closeBtn = document.querySelector('.popup__close')
const popup = document.querySelector('.popup__wrapper')
popup.addEventListener('click', (e) => {
    if (e.target === popup) {
        document.querySelector('body').style.overflow = 'unset'
        popup.style.display = 'none'
    }
})

closeBtn.addEventListener('click', () => {
    document.querySelector('body').style.overflow = 'unset'
    popup.style.display = 'none'
})

// Form
const submitForm = document.querySelector('.form__submit')
submitForm.addEventListener('click', function (event) {
    document.querySelector('body').style.overflow = 'hidden'
    event.preventDefault()
    popup.style.display = 'block'
})


// Responsive
const windowWidth = window.innerWidth
if (windowWidth < 1455) {
    document.querySelector('.first-screen__course').innerText = 'передзапис на курс'
    document.querySelector('.first-screen__btn').innerText = 'Передзапис'
}

// scroll to feedback

function scrollTo(element) {
    windowWidth.scroll({
        left: 0,
        top: element.offsetTop,
        behavior: 'smooth'
    })
}

var btn = document.querySelector('.first-screen__btn');
var feedback = document.querySelector('#feedback');
console.log(btn)
btn.addEventListener('click', function(event) {
  event.preventDefault();
  feedback.scrollIntoView({ behavior: 'smooth' });
});
