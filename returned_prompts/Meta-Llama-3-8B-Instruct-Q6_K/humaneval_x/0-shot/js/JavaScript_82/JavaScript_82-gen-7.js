Here is the solution for the problem:

```javascript
const primeLength = (string) => {
  const length = string.length;
  if (length < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(length); i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
};
```

Explanation:

1. First, we calculate the length of the input string.
2. We check if the length is less than 2. If it is, we return false because 0 and 1 are not prime numbers.
3. We loop through all numbers from 2 to the square root of the length (inclusive).
4. For each number, we check if the length is divisible by that number. If it is, we return false because the length is not a prime number.
5. If the loop completes without finding a divisor, we return true because the length is a prime number.

This solution works because all prime numbers are of the form 6k ± 1, where k is a positive integer. This is known as the Sieve of Eratosthenes. By only checking divisibility up to the square root of the length, we can efficiently determine whether the length is a prime number or not.