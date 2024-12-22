document.getElementById('sendButton').addEventListener('click', function () {
    // Lấy dữ liệu từ input
    const data = document.getElementById('dataInput').value;

    // Gửi request AJAX tới server
    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: data }),
    })
        .then((response) => response.json())
        .then((data) => {
            // Hiển thị phản hồi từ server
            if (data.success) {
                document.getElementById('responseText').innerText = data.response;
            } else {
                document.getElementById('responseText').innerText = 'Error: ' + data.response;
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});
