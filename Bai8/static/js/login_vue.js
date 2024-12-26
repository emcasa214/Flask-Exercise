const { createApp } = Vue;
createApp({
    data() {
        return {
            username: '',
            password: '',
            message: '',
            isSuccess: false,
        }
    },
    methods: {
        async submitLogin() {
            try {
                const response = await axios.post('/', {
                    username: this.username,
                    password: this.password
                });
                // Kiểm tra phản hồi
                if (response && response.data) {
                    this.message = response.data.message;
                    this.isSuccess = response.data.success
                } else {
                    this.message = "Phản hồi không hợp lệ từ server.";
                    this.isSuccess = false
                }
            } catch (error) {
                console.error('Error:', error);
                this.message = 'Đã xảy ra lỗi khi gửi yêu cầu.';
                this.isSuccess = false
            }
        }
    }
}).mount('#app')
