document.getElementById('recipeForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const flour = document.getElementById('flour').value;
    const sugar = document.getElementById('sugar').value;

    // Validate input: check if flour and sugar are numeric
    if (!isNumeric(flour)) {
        displayError('flourError', 'Please enter a numeric value');
    } else {
        clearError('flourError');
    }

    if (!isNumeric(sugar)) {
        displayError('sugarError', 'Please enter a numeric value');
    } else {
        clearError('sugarError');
    }

    // Check if either flour or sugar has an error message
    if (!isNumeric(flour) || !isNumeric(sugar)) {
        return; // Stop further processing if there are errors
    }

    const formData = new FormData(this);
    const formDataObject = Object.fromEntries(formData.entries());

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formDataObject)
    });

    const data = await response.json();
    document.getElementById('predictionResult').innerText = data.prediction;
    const predictionResult = document.getElementById('predictionResult');
    predictionResult.innerText = data.prediction;
    // Update the prediction result
    predictionResult.classList.add('prediction-text');

});

function isNumeric(value) {
    return !isNaN(parseFloat(value)) && isFinite(value);
}

function displayError(errorId, errorMessage) {
    const errorElement = document.getElementById(errorId);
    errorElement.classList.add('error');
    errorElement.innerText = errorMessage;
}

function clearError(errorId) {
    const errorElement = document.getElementById(errorId);
    errorElement.classList.remove('error');
    errorElement.innerText = '';
}
