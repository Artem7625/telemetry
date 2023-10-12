const getDataButton = document.getElementById("getData");
const responseDataDiv = document.getElementById("responseData");
const nameInput = document.getElementById("nameInput");
const postDataButton = document.getElementById("postData");

getDataButton.addEventListener("click", async () => {
    try {
        const response = await fetch("/service/name", {
            method: "GET"
        });
        const data = await response.json();
        responseDataDiv.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        responseDataDiv.textContent = "Error occurred: " + error.message;
    }
});

postDataButton.addEventListener("click", async () => {
    try {
        const name = nameInput.value;
        const response = await fetch("/service/name", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name
            })
        });

        if (response.status === 200) {
            alert("Engineer name set successfully!");
        } else {
            alert("Failed to set engineer name.");
        }
    } catch (error) {
        alert("Error occurred: " + error.message);
    }
});