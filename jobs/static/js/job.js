$().ready(function() {
    History = window.History;
    ldmks = $('header nav a');
    pages = $('.page');
    index = 0;
    initial_state = $(ldmks[0]).attr('href').substr(1);
    initial_title = $(ldmks[0]).text();
    base_title = $('meta[name=base-title]').attr('content');

    ldmks.click(function(e) {
        e.preventDefault();
        index = ldmks.index(this);
        var current_state = History.getState().data.page;
        var previous_index = pages.index($('#'+current_state));
        var section_name = $(this).attr('href').substr(1);
        var new_title = $(this).text() + base_title;
        $('nav a').removeClass('here');
        $(this).addClass('here');
        $('body').removeClass('show-'+previous_index).addClass('show-'+index);
        History.pushState({page: section_name}, new_title, '?'+section_name);
    });

    $('.pageWrapper').click(function(e) {
        section = $(this).parent().attr('id');
        $('#ldmk_'+section).click();
    });

    $(window).keyup(function(e) {
        if (e.keyCode == 39 && index < ldmks.length-1) {
            $(ldmks[index+1]).click();
        } else if (e.keyCode == 37 && index > 0) {
            $(ldmks[index-1]).click();
        }
    });

    pages.each(function(i, page) {
        mright = (pages.length-1 - i) * 3;
        zindex = (pages.length-1 - i) * 10;
        width = 100 - ((pages.length-1 - i) * 5);
        $(page).addClass('page-'+i).css({
            'margin-right': mright+'em',
            'z-index': zindex,
            'width': width+'%'
        });
    });

    if (window.location.search == "") {
        History.pushState({page: initial_state}, initial_title+base_title, '?'+initial_state);
    } else {
        History.pushState({page: initial_state}, initial_title+base_title, '');
        $('#ldmk_'+window.location.search.substr(1)).click();
    }

});