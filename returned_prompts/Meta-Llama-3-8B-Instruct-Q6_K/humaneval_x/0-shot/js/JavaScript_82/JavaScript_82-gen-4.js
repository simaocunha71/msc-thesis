Here is a simple function that solves the problem:
```
const primeLength = (string) => {
  const length = string.length;
  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };
  return isPrime(length);
};
```
Here's an explanation of how the function works:

1. We first get the length of the input string using the `length` property.
2. We define a helper function `isPrime` that takes an integer `n` as input and returns `true` if `n` is a prime number, and `false` otherwise. The function uses the trial division method to check if `n` is prime.
3. We call the `isPrime` function with the length of the input string as the argument, and return the result.

You can test the function with the examples you provided:
```
console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
```
I hope this helps! Let me know if you have any questions. 😊

Note: This function assumes that the input string is not empty. If you want to handle the case where the input string is empty, you can add a simple check at the beginning of the function:
```
const primeLength = (string) => {
  if (!string) return false;
  // rest of the function remains the same
};
```
This way, if the input string is empty, the function will return `false` immediately. 😊