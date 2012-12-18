$(function() {
    // trick to give a select menu an initial value
    $('select[data-value]').each(function () {
        var val = $(this).attr('data-value');
        if (val) {
            $(this).find('option').removeAttr('selected');
            $(this).find('option[value="' + val + '"]').attr('selected', 'true');
        }
    });

    $('.announcement-control').on('click', function () {
        $.ajax({
            url: '/announcements/clear/'+$(this).data('announcementid')
        });
    });
});

$.fn.hqHelp = function () {
    var self = this;
    self.each(function(i) {
        var $helpElem = $($(self).get(i));
        $helpElem.find('i').popover();
        $helpElem.click(function () {
            if ($helpElem.find('i').attr('data-trigger') != 'hover') {
                $(this).toggleClass('on');
            }
            if ($(this).hasClass('no-click')) {
                return false;
            }
        })
    });
};
