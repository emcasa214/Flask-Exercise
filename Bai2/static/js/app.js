document.addEventListener("DOMContentLoaded", () => {
    const noteInput = document.getElementById("note-input");
    const saveButton = document.getElementById("save-button");
    const notesList = document.getElementById("notes-list");

    // gọi api lấy tất cả các note được lưu
    fetch("/notes")
        .then(response => response.json())
        .then(data => {
            data.forEach(note => {
                const li = document.createElement("li");
                li.textContent = note.text;
                notesList.appendChild(li);
            });
        });

    // khi nút saveButton được click 
    saveButton.addEventListener("click", () => {
        const noteText = noteInput.value;
        if (!noteText) return;

        //gọi api để gửi dữ liệu người dùng nhập ở noteInput
        fetch("/notes", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text: noteText }),
        })
            .then(response => response.json())
            .then(() => {
                const li = document.createElement("li");
                li.textContent = noteText;
                notesList.appendChild(li);
                noteInput.value = "";
            });
    });
});
