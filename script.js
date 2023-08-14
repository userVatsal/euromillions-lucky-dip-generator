function generateLuckyDip() {
    const mainNumbers = getRandomNumbers(5, 1, 50);
    const luckyStars = getRandomNumbers(2, 1, 12);

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h3>Main Numbers: <span class="numbers">${mainNumbers.join(', ')}</span></h3>
        <h3>Lucky Stars: <span class="numbers">${luckyStars.join(', ')}</span></h3>
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
