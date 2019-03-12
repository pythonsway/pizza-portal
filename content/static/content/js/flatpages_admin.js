$(function () {
    const idContent = $('#id_content');
    $('#wysiwyg').trumbowyg()
        .on('tbwinit', function () { idContent.hide(); })
        .on('tbwchange', function (e) { idContent.val(e.target.innerHTML); });
});
