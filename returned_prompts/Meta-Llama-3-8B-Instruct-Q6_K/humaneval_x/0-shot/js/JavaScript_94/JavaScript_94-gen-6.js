```javascript
const skjkasdkd = (lst) => {
    let maxPrime = 0;
    for (let i = 0; i < lst.length; i++) {
        if (isPrime(lst[i]) && lst[i] > maxPrime) {
            maxPrime = lst[i];
        }
    }
    return sumOfDigits(maxPrime);
};

const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
        if (num % i === 0) return false;
    }
    return true;
};

const sumOfDigits = (num) => {
    let sum = 0;
    while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }
    return sum;
};
``` 