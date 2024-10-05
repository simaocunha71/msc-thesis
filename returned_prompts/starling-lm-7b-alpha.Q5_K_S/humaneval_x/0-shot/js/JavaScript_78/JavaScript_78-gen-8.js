
function hexToDecimal(hex) {
    const hexToDecimalMap = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    };

    let total = 0;
    let multiplier = 16;

    hex.split('').reverse().forEach(char => {
        total += hexToDecimalMap[char] * multiplier;
        multiplier /= 16;
    });

    return total;
}

function isPrime(num) {
    if (num < 2 || num % 2 === 0) {
        return false;
    }
    if (num === 2) {
        return true;
    }
    for (let i = 3; i * i <= num; i += 2) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

function hexToPrimeCount(hex) {
    let count = 0;

    hex.split('').forEach(char => {
        const num = hexToDecimal(char);
        if (isPrime(num)) {
            count++;
        }
    });

    return count;
}

console.log(hexToPrimeCount("ABED1A33"));
console.log(hexToPrimeCount("123456789ABCDEF0"));
console.log(hexToPrimeCount("AB"));
console.log(hexToPrimeCount("1077E"));
console.log(hexToPrimeCount("2020"));

















