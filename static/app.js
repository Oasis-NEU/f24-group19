document.addEventListener("DOMContentLoaded", () => {
    const app = document.getElementById("app");

    // Create UI elements
    const title = document.createElement("h1");
    title.textContent = "Clothing Recommendation System";
    app.appendChild(title);

    const trainButton = document.createElement("button");
    trainButton.textContent = "Train Model";
    trainButton.addEventListener("click", async () => {
        try {
            const response = await fetch("/train", { method: "POST" });
            const result = await response.json();
            alert(result.message);
        } catch (error) {
            alert("Error training the model.");
        }
    });
    app.appendChild(trainButton);

    app.appendChild(document.createElement("hr"));

    const formTitle = document.createElement("h2");
    formTitle.textContent = "Predict Clothing Category";
    app.appendChild(formTitle);

    const form = document.createElement("form");

    const fields = [
        { id: "top_bot", label: "Top or Bottom", type: "text", placeholder: "e.g., bottom" },
        { id: "color", label: "Color", type: "text", placeholder: "e.g., green" },
        { id: "length", label: "Length", type: "text", placeholder: "e.g., long" },
        { id: "style", label: "Style", type: "text", placeholder: "e.g., slacks" },
    ];

    fields.forEach((field) => {
        const label = document.createElement("label");
        label.textContent = `${field.label}: `;
        const input = document.createElement("input");
        input.type = field.type;
        input.id = field.id;
        input.placeholder = field.placeholder;
        form.appendChild(label);
        form.appendChild(input);
        form.appendChild(document.createElement("br"));
    });

    const submitButton = document.createElement("button");
    submitButton.textContent = "Predict";
    submitButton.type = "submit";
    form.appendChild(submitButton);

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const newItem = {};
        fields.forEach((field) => {
            const input = document.getElementById(field.id);
            newItem[field.id] = input.value;
        });

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newItem),
            });

            const result = await response.json();
            if (result.error) {
                alert(`Error: ${result.error}`);
            } else {
                alert(`Predicted Category: ${result.predicted_category}`);
            }
        } catch (error) {
            alert("Error predicting the category.");
        }
    });

    app.appendChild(form);
});
