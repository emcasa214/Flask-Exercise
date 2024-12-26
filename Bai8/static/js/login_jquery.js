$(document).ready(function () {
    $('#loginForm').on('submit', function (e) {
        e.preventDefault(); // Ngăn việc submit form truyền thống
        const formData = {
            username: $('#username').val(),
            password: $('#password').val()
        };
        // Gửi dữ liệu qua AJAX
        $.ajax({
            url: '/',
            method: 'POST',
            data: formData,
            success: function (response) {
                if (response.success) {
                    $('#responseMessage').text(response.message).css('color', 'green');
                } else {
                    $('#responseMessage').text(response.message).css('color', 'red');
                }
            },
            error: function () {
                $('#responseMessage').text('Đã xảy ra lỗi trong quá trình gửi yêu cầu.').css('color', 'red');
            }
        });
    });
});
