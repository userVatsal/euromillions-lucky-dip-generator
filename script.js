function generateLuckyDip() {
    // Example logic to generate a random EuroMillions ticket
    // You may replace this logic with a more sophisticated algorithm based on your constraints
    const mainNumbers = getRandomNumbers(5, 1, 50);
    const luckyStars = getRandomNumbers(2, 1, 12);

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h3>Main Numbers: ${mainNumbers.join(', ')}</h3>
        <h3>Lucky Stars: ${luckyStars.join(', ')}</h3>
    `;
}

function getRandomNumbers(count, min, max) {
    const numbers = [];
    while (numbers.length < count) {
        const num = Math.floor(Math.random() * (max - min + 1)) + min;
        if (!numbers.includes(num)) {
            numbers.push(num);
        }
    }
    return numbers.sort((a, b) => a - b);
}
