Here is a possible implementation of the `primeLength` function in JavaScript:
```
const primeLength = (string) => {
  const length = string.length;
  if (length <= 1) return false;
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) return false;
  }
  return true;
};
```
Here's an explanation of the code:

1. We first check if the length of the string is less than or equal to 1, in which case it's not a prime number, so we return `false`.
2. We then loop through all numbers from 2 to the square root of the string length (inclusive).
3. For each number `i`, we check if the string length is divisible by `i` by using the modulo operator (`%`). If it is, then the string length is not a prime number, so we return `false`.
4. If the loop completes without finding a divisor, then the string length is a prime number, so we return `true`.

You can test this function with the examples you provided:
```
console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
```
Note that this function only checks if the string length is a prime number, not whether the string itself contains any prime numbers. If you want to check that, you would need a different approach.