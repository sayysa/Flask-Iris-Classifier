function predict() {
    // Get input values from the form
    const sepalLength = parseFloat(document.getElementById('sepalLength').value);
    const sepalWidth = parseFloat(document.getElementById('sepalWidth').value);
    const petalLength = parseFloat(document.getElementById('petalLength').value);
    const petalWidth = parseFloat(document.getElementById('petalWidth').value);

    // Send input data to Flask backend using fetch API
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sepalLength: sepalLength,
            sepalWidth: sepalWidth,
            petalLength: petalLength,
            petalWidth: petalWidth
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display the prediction result
        const predictionResult = document.getElementById('predictionResult');
        predictionResult.innerHTML = `<p>Prediction: ${data.prediction}</p>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
