To solve this problem, you can follow these steps:

1. Calculate the length of the input string.
2. Check if the length is a prime number or not.

Here's the complete code:

```javascript
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const primeLength = (string) => {
  const length = string.length;
  return isPrime(length);
};

console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
```

In this code, the `isPrime` function checks if a number is prime or not. It iterates from 2 to the square root of the number and checks if the number is divisible by any of these values. If it is divisible, the function returns false; otherwise, it returns true.

The `primeLength` function calculates the length of the input string and calls the `isPrime` function to check if the length is prime or not. Finally, it returns the result.