```javascript
const isMultiplyPrime = (a) => {
  let count = 0;
  for (let i = 2; i <= a; i++) {
    if (isPrime(i)) {
      for (let j = i; j <= a / i; j++) {
        if (isPrime(j) && a % (i * j) === 0) {
          count++;
          if (count === 3) {
            return true;
          }
        }
      }
    }
  }
  return false;
};

const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```

Explanation:
This problem is solved by creating a function `isMultiplyPrime` which checks if a given number is the multiplication of three prime numbers. The function uses another helper function `isPrime` to check if a number is prime.

In the `isMultiplyPrime` function, we loop through all numbers from 2 to `a` and for each number, we loop through all numbers from that number to `a / i` and check if both numbers are prime and `a` is divisible by their product. If we find three such prime numbers, we return `true`.

The `isPrime` function checks if a number is prime by checking if it is divisible by any number up to its square root. If it is divisible, it is not a prime number, otherwise, it is a prime number.

The time complexity of this solution is O(a^2) because we are looping through all numbers up to `a` and for each number, we are looping through all numbers up to `a / i`. The space complexity is O(1) because we are using a constant amount of space to store the count and the result.