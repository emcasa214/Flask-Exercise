document.addEventListener("DOMContentLoaded",() =>{
    const inputText =  document.getElementById("inputText")
    const buttonClick =  document.getElementById("buttonClick")

    buttonClick.addEventListener("click", () => {
        const name = inputText.value;
        fetch("/hello" , {
            method: "POST",
            headers:{
                "Content-Type": "application/json",
            },
            body: JSON.stringify({name: name})
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("response").textContent = data.message;
        })
        .catch(error => {
            console.error("Error: ",error);
            document.getElementById("response").textContent = "Đã xảy ra lỗi";
        })
    });
});