```javascript
const isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0) return false;
    }
    return true;
};

const isMultiplyPrime = (a) => {
    let count = 0;
    for (let i = 2; i <= Math.sqrt(a); i++) {
        if (a % i === 0 && isPrime(i)) {
            count++;
            if (count === 3) return true;
        }
    }
    return false;
};
```
Explanation:
1. `isPrime(num)`: This function checks if a number is prime or not. It iterates from 2 to `num` and checks if any number divides `num` evenly. If it does, then `num` is not prime, otherwise it is prime.
2. `isMultiplyPrime(a)`: This function checks if a number is the multiplication of 3 prime numbers. It iterates from 2 to the square root of `a` and checks if any number divides `a` evenly. If it does and the number is prime, then the count of prime numbers is increased. If the count of prime numbers reaches 3, then `a` is the multiplication of 3 prime numbers, otherwise it is not.