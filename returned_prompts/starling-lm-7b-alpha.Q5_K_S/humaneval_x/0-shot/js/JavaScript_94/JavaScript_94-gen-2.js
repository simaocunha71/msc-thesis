
let max = 0;
let sum = 0;

for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
        let sum = sumOfDigits(lst[i]);
        if (sum > max) {
            max = sum;
        }
    }
}

return max;

};

function isPrime(num) {
    if (num < 2) return false;
    if (num === 2 || num === 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    let i = 5;
    while (i * i <= num) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
        i += 6;
    }
    return true;
}

function sumOfDigits(num) {
    let sum = 0;
    while (num) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }
    return sum;
}











































































































































































































































