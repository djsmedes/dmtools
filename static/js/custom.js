$(document).ready(function () {
    $('.clickable-row').click(function () {
        window.location = $(this).data("href");
    });
});

$(document).ready(function () {
    $('.combatant-context-enter').click(function () {
        var combatant = $(this).data("combatant");
        $('.combatant-context-hide').hide();
        $('.combatant-context-show').show();
        $('.combatant-context-hide-unmatch').each(function () {
            if ($(this).data("combatant") !== combatant) {
                $(this).hide()
            }
        });
        $('.combatant-context-hide-match').each(function () {
            if ($(this).data("combatant") === combatant) {
                $(this).hide()
            }
        });
    });
    $('.combatant-context-leave').click(function () {
        var combatant = $(this).data("combatant");
        $('.combatant-context-hide').show();
        $('.combatant-context-show').hide();
        $('.combatant-context-hide-unmatch').each(function () {
            if ($(this).data("combatant") !== combatant) {
                $(this).show()
            }
        });
        $('.combatant-context-hide-match').each(function () {
            if ($(this).data("combatant") === combatant) {
                $(this).show()
            }
        });
    });
    $('.enter-buff-apply-context').click(function () {
        $('.apply-context-hide').hide();
        $('.apply-context-show').show();
        localStorage.setItem('effect-context', 'buff');
    });
    $('.enter-debuff-apply-context').click(function () {
        $('.apply-context-hide').hide();
        $('.apply-context-show').show();
        localStorage.setItem('effect-context', 'debuff');
    });
    $('.enter-other-apply-context').click(function () {
        $('.apply-context-hide').hide();
        $('.apply-context-show').show();
        localStorage.setItem('effect-context', 'other');
    });
    $('.exit-apply-context').click( exit_apply_context );

    $('#effect-to-apply').on("change paste keyup", function () {
        if ($(this).val() === '') {
            $('#apply-button').html('Cancel').prop('type', 'button').addClass('exit-apply-context')
        } else {
            $('#apply-button').html('Apply').prop('type', 'submit').removeClass('exit-apply-context')
        }
    });

    $('.apply-context-activatable').click(function () {
        $(this).toggleClass('active');
        var effect = '';
        if ($(this).hasClass('active')) {
            effect = $('#effect-to-apply').val()
        }
        var combatant = $(this).data('combatant');
        var id = '#' + combatant + '-' + localStorage.getItem('effect-context');
        $(id).val(effect);
    });
});

function exit_apply_context() {
    $('.apply-context-hide').show();
    $('.apply-context-show').hide();
    localStorage.setItem('effect-context', '');
    $('.effect-input').val('');
    $('.apply-context-activatable').removeClass('active');
}
