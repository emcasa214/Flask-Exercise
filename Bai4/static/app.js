document.getElementById('registerForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const password = document.getElementById('registerPassword').value;
    const hashedPassword = sha256(password);

    const response = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ hashed_password: hashedPassword }),
    });
    const result = await response.json();
    document.getElementById('message').innerText = result.message || result.error;
});

document.getElementById('loginForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const password = document.getElementById('loginPassword').value;
    const hashedPassword = sha256(password);

    const response = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ hashed_password: hashedPassword }),
    });
    const result = await response.json();
    document.getElementById('message').innerText = result.message || result.error;
});

// SHA-256 mã hóa ở phía client
function sha256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    return crypto.subtle.digest('SHA-256', msgBuffer).then((hashBuffer) => {
        return Array.from(new Uint8Array(hashBuffer))
            .map(b => b.toString(16).padStart(2, '0'))
            .join('');
    });
}
