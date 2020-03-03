var main_input = document.getElementById('main-input');
var main_textfield = document.querySelector('.main-textfield');
var tags = [];
var offset = 0;

document.querySelector('.main-overlay').addEventListener('click',function()
{
    $('.main-overlay').css({transform: 'scale(0)',opacity: 0});
});

document.getElementById('search_button').addEventListener('click',function()
{
    Search();
});

window.addEventListener('keypress',function(event)
{
    if(event.keyCode == 13)
    {
        event.preventDefault();
        Search();
    }
})

$('.suggestion').click(function()
{
    var current_text = $(this).children()[0].innerText;

    if(tags.includes(current_text))
    {
        return;
    }

    var current = $(this).clone();
    current.appendTo('.suggestions');
    var element = current.children()[0].innerText;
    tags.push(element);
    main_input.value += current_text + " ";
});

function Search()
{
    var duration = 0.4;
    var main_delay = 0.7;
    TweenMax.to('#main-form',1.3,{y: -230,ease: Elastic.easeInOut.config(1, 0.8)});
    TweenMax.to("nav",duration,{backgroundColor: '#55AF6B',delay: main_delay});
    TweenMax.to("html",duration,{backgroundColor: 'white',delay: main_delay});
    TweenMax.to('.main-content h1, .main-content h2, .form-suggestions',0.5,{opacity: 0});
    TweenMax.to('.main-monster',2,{opacity: 0,y: -2000,ease: Elastic.easeInOut.config(1, 0.8)});
    TweenMax.to('.main-background',2,{y: -2000,delay: 0.8});
    TweenMax.to('.page-2',0.5,{opacity: 1,visibility: 'visible',delay: 1.3});
    TweenMax.to('.result',0.5,{opacity: 1,visibility: 'visible',delay: 1.4});

    $.ajax({
        type: 'POST',
        url: '/',
        data: $('#main-form').serialize(),
        success: function (q)
        {
            var image = document.getElementById('main-image');
            document.querySelector('.result').style.transform = "translateY(0)";
            document.querySelector('.result-text').style.display = 'none';
            image.style.width = "80%";
            image.style.opacity = 1;
            image.src = q;

            image.addEventListener('click',function()
            {
                $('.main-overlay').css({transform: 'scale(1)',opacity: 1});
                $('.main-overlay img').css({transform: 'scale(1)',opacity: 1});
                var full = document.getElementById('full-image');
                full.src = q;
            });
        }
    });
}