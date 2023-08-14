function generateLuckyDip() {
    const evenOddBalanceElement = document.getElementById('even-odd-balance');
    if (!evenOddBalanceElement) return showError('Even-odd balance element not found!');

    const evenOddBalance = evenOddBalanceElement.value;
    const mainNumbers = getRandomNumbers(5, 50, evenOddBalance);
    const luckyStars = getRandomNumbers(2, 12);

    if (mainNumbers.length === 0 || luckyStars.length === 0) {
        return showError('Failed to generate lucky dip! Please try again.');
    }

    const resultHtml = getResultHtml(mainNumbers, luckyStars);
    document.getElementById('result').innerHTML = resultHtml;
}

function isNumberValid(num, evenOddBalance) {
    return evenOddBalance === 'balanced' ||
           (evenOddBalance === 'even' && num % 2 === 0) ||
           (evenOddBalance === 'odd' && num % 2 !== 0);
}

function getRandomNumbers(count, max, evenOddBalance = 'balanced') {
    if (count < 1 || max < count) {
        console.error('Invalid parameters for generating random numbers!');
        return [];
    }

    const numbers = new Set();
    const range = max + 1;
    while (numbers.size < count) {
        let num = Math.floor(Math.random() * range);
        if (isNumberValid(num, evenOddBalance)) numbers.add(num);
    }
    return Array.from(numbers).sort((a, b) => a - b);
}

function getResultHtml(mainNumbers, luckyStars) {
    return `
        <h3>Main Numbers: <span class="numbers">${mainNumbers.join(', ')}</span></h3>
        <h3>Lucky Stars: <span class="numbers">${luckyStars.join(', ')}</span></h3>
    `;
}

function showError(message) {
    alert(message);
    console.error(message);
}

