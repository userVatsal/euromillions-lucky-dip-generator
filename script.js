function generateLuckyDip() {
    // Generate a random EuroMillions ticket
    const mainNumbers = getRandomNumbers(5, 1, 50);
    const luckyStars = getRandomNumbers(2, 1, 12);

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h3>Main Numbers: ${mainNumbers.join(', ')}</h3>
        <h3>Lucky Stars: ${luckyStars.join(', ')}</h3>
    `;
}

function getRandomNumbers(count, min, max) {
    const numbers = new Set();
    while (numbers.size < count) {
        const num = Math.floor(Math.random() * (max - min + 1)) + min;
        numbers.add(num);
    }
    return Array.from(numbers).sort((a, b) => a - b);
}
