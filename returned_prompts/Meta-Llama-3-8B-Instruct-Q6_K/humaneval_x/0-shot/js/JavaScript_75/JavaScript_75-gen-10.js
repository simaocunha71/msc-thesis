Here is a JavaScript function that fulfills the requirement:
```javascript
const isMultiplyPrime = (a) => {
  let count = 0;
  for (let i = 2; i <= a; i++) {
    if (isPrime(i)) {
      let temp = a / i;
      if (temp % 1 === 0) {
        for (let j = 2; j <= temp; j++) {
          if (isPrime(j)) {
            let temp2 = temp / j;
            if (temp2 % 1 === 0) {
              for (let k = 2; k <= temp2; k++) {
                if (isPrime(k)) {
                  count++;
                }
              }
            }
          }
        }
      }
    }
  }
  return count === 3;
};

const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
In this code, we define a helper function `isPrime` to check if a number is prime. Then, the `isMultiplyPrime` function checks if the given number `a` can be divided by three prime numbers. It does this by iterating over all numbers from 2 to `a`, checking if each number is prime, and if it is, then checking if `a` divided by that number can also be divided by two other prime numbers. If we find three prime numbers that multiply to `a`, we return `true`; otherwise, we return `false`.

Note: This function may not be efficient for large numbers, as it checks every number from 2 to `a` to see if it is prime. For a more efficient solution, you could use a sieve to generate all prime numbers up to `a` and then check if `a` can be divided by three of them. However, for small numbers like the ones in the example, this function should work fine.