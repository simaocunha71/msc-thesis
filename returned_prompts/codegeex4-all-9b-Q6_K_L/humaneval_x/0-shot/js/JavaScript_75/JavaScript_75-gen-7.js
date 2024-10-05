Here is a solution written in JavaScript:

```javascript
const isMultiplyPrime = (a) => {
    // Helper function to check if a number is prime
    const isPrime = (num) => {
        if (num < 2) return false;
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    };

    // Check if the input number is less than 2
    if (a < 2) return false;

    // Check if the input number is a prime
    if (isPrime(a)) return false;

    // Check if the input number is a multiplication of 3 prime numbers
    let factors = [];
    for (let i = 2; i <= a; i++) {
        if (a % i === 0 && isPrime(i)) {
            factors.push(i);
        }
        if (factors.length > 3) return false;
    }
    return factors.length === 3;
};

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(40)); // false
console.log(isMultiplyPrime(7)); // false
console.log(isMultiplyPrime(6)); // false
```

This function first checks if the input number is less than 2, if so, it returns false. Then it checks if the input number is a prime, if so, it returns false. If the input number is not less than 2 and not a prime, it finds the factors of the number and checks if there are exactly 3 prime factors. If there are, it returns true, otherwise, it returns false.