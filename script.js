function generateLuckyDip() {
    const evenOddBalance = document.getElementById('even-odd-balance').value;
    const mainNumbers = getRandomNumbers(5, 1, 50, evenOddBalance);
    const luckyStars = getRandomNumbers(2, 1, 12);

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h3>Main Numbers: <span class="numbers">${mainNumbers.join(', ')}</span></h3>
        <h3>Lucky Stars: <span class="numbers">${luckyStars.join(', ')}</span></h3>
    `;
}

function getRandomNumbers(count, min, max, evenOddBalance = 'balanced') {
    const numbers = new Set();
    while (numbers.size < count) {
        let num = Math.floor(Math.random() * (max - min + 1)) + min;
        if (evenOddBalance === 'even' && num % 2 !== 0) continue;
        if (evenOddBalance === 'odd' && num % 2 === 0) continue;
        numbers.add(num);
    }
    return Array.from(numbers).sort((a, b) => a - b);
}
