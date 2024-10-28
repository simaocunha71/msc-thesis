```javascript
const countUpTo = (n) => {
    if (n <= 1) return [];
    const primes = [];
    for (let i = 2; i < n; i++) {
        let isPrime = true;
        for (let j = 2; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) primes.push(i);
    }
    return primes;
};
```
The above solution iterates through all numbers from 2 to n-1 and checks if each number is prime. If it is, it adds it to the `primes` array. Finally, it returns the `primes` array.