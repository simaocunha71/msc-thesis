Here is a solution in JavaScript:

```javascript
function isMultiplyPrime(a) {
    let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
    let factors = [];
    for (let i = 0; i < primes.length; i++) {
        if (a % primes[i] === 0) {
            factors.push(primes[i]);
            a /= primes[i];
            i = -1;
        }
        if (a === 1) {
            break;
        }
    }
    if (factors.length === 3 && a === 1) {
        return true;
    }
    return false;
}

console.log(isMultiplyPrime(30)); // true
```

Explanation:

The function `isMultiplyPrime(a)` checks whether the given number `a` is the multiplication of 3 prime numbers or not. 

The function `isMultiplyPrime(a)` uses an array `primes` which contains the first 25 prime numbers. 

The function `isMultiplyPrime(a)` uses a for loop to iterate over the `primes` array. 

For each prime number, the function `isMultiplyPrime(a)` checks whether `a` is divisible by the prime number. If `a` is divisible by the prime number, the prime number is added to the `factors` array and `a` is divided by the prime number. 

The function `isMultiplyPrime(a)` continues this process until `a` is no longer divisible by any prime number. 

If `a` is divided by all prime numbers and the length of the `factors` array is 3, the function `isMultiplyPrime(a)` returns `true`. Otherwise, the function `isMultiplyPrime(a)` returns `false`.