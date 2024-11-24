document.getElementById("trainButton").addEventListener("click", async () => {
    const response = await fetch("/train", { method: "POST" });
    const result = await response.json();
    alert(result.message || "Model trained successfully!");
});

document.getElementById("predictForm").addEventListener("submit", async (event) => {
    event.preventDefault();  // Prevent default form submission

    // Collect form data
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    // Remove 'n_predictions' from the data since it's not a feature for the model
    const { n_predictions, ...predictData } = data;

    try {
        // Send POST request to the /predict endpoint with the form data
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(predictData)  // Send data as JSON
        });

        const predictionsContainer = document.getElementById("predictions");
        predictionsContainer.innerHTML = "";  // Clear any existing predictions

        if (response.ok) {
            const result = await response.json();

            if (result.predicted_categories && result.predicted_categories.length > 0) {
                result.predicted_categories.forEach((imageName) => {
                    const predictionDiv = document.createElement("div");

                    const img = document.createElement("img");
                    img.src = `/get_image/${imageName}`;
                    img.alt = imageName;

                    const label = document.createElement("p");
                    label.textContent = imageName;

                    predictionDiv.appendChild(img);
                    predictionDiv.appendChild(label);
                    predictionsContainer.appendChild(predictionDiv);
                });
            } else {
                predictionsContainer.innerHTML = "<p>No predictions found.</p>";
            }
        } else {
            const error = await response.json();
            alert(error.error || "An error occurred while predicting.");
        }
    } catch (error) {
        console.error("Error during prediction request:", error);
        alert("Failed to predict. Please try again.");
    }
});
