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

// $('js-order-delete').on('click', function () {
//     var btn = $(this);
//     $.ajax({
//         url: btn.attr("data-url"),
//         type: 'post',
//         dataType: 'json',
//         success: function (data) {
//             $("#modal-book .modal-content").html(data.html_form);
//         }
//     });
// };

//     );

// var saveForm = function () {
//     var form = $(this);
//     $.ajax({
//         url: form.attr("action"),
//         data: form.serialize(),
//         type: form.attr("method"),
//         dataType: 'json',
//         success: function (data) {
//             if (data.form_is_valid) {
//                 $("#book-table tbody").html(data.html_book_list);
//                 $("#modal-book").modal("hide");
//             }
//             else {
//                 $("#modal-book .modal-content").html(data.html_form);
//             }
//         }
//     });
//     return false;
// };


// /* Binding */

// // Create book
// $(".js-create-book").click(loadForm);
// $("#modal-book").on("submit", ".js-book-create-form", saveForm);

// // Update book
// $("#book-table").on("click", ".js-update-book", loadForm);
// $("#modal-book").on("submit", ".js-book-update-form", saveForm);

// // Delete book
// $("#book-table").on("click", ".js-delete-book", loadForm);
// $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

// });
