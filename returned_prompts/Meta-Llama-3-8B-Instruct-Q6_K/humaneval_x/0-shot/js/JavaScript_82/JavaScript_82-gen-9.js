Here is the solution:
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
Explanation:

1. We first check if the length of the string is less than or equal to 1, in which case it's not a prime number, so we return false.
2. We then iterate from 2 to the square root of the length of the string (inclusive) to check if the length is divisible by any of these numbers. If it is, we return false.
3. If the length is not divisible by any of these numbers, we return true, indicating that the length is a prime number.

Testing:

```
console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
```

This solution works by checking if the length of the string is a prime number. A prime number is a positive integer that is divisible only by itself and 1. The function uses a loop to check if the length is divisible by any number up to its square root. If it is, it returns false, indicating that the length is not a prime number. If it's not divisible by any of these numbers, it returns true, indicating that the length is a prime number. This solution is efficient because it only checks divisibility up to the square root of the length, which reduces the number of iterations needed.