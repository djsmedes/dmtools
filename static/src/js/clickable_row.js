module.exports = {

    initialize: function() {
        $('.clickable-row').click(function () {
            window.location = $(this).data("href");
        });
    }

};
