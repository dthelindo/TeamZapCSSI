para = $("para");

/* Needed for paragraphs above the screen threshold, otherwise they wouldn't appear until scroll*/
para.each(function () {
    a = $(this).offset().top + (0.5 * $(this).height());
    b = $(window).height();
    if (a< b) $(this).addClass("paraFadeIn");
});

$(window).scroll(function () {
    para.each(function () {
        a = $(this).offset().top + (0.5 * $(this).height());
        b = $(window).scrollTop() + $(window).height();
        if (a < b) $(this).addClass("paraFadeIn");
    });
});
