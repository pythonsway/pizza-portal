$(function () {
    // choosing 'toppings'
    const numToppings = $('#id_toppings_num').val();
    $('#add2cart').prop('disabled', (numToppings > 0));
    $('#id_toppings').on('change', function (e) {
        $('#add2cart').prop('disabled', ($('#id_toppings option:selected').length != numToppings));
    });

    // alerts auto-close
    window.setTimeout(function () {
        $('.alert').alert('close');
    }, 3000);

    // AJAX cart item
    $('#js-orderitems-include').on('submit', '.js-orderitem-delete', function () {
        const form = $(this);
        form.closest('tr').hide(1000, function () {
            $.ajax({
                url: form.attr('action'),
                data: form.serialize(),
                type: form.attr('method'),
                dataType: 'json',
                success: function (data) {
                    $('#js-orderitems-include').html(data.orderitem_list);
                    let xButtons = $('.js-orderitem-delete');
                    $('#js-orderitems-number').text(xButtons.length);
                    $('#js-checkout').attr('hidden', (xButtons.length < 1));
                }
            });
        });
        return false;
    });
});
