Here is the solution for the problem:

```javascript
const primeLength = (string) => {
  const length = string.length;
  if (length <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++) {
    if (length % i === 0) return false;
  }
  return true;
};
```

This function works by first checking if the length of the string is less than or equal to 1, in which case it returns false (since 0 and 1 are not prime numbers). Then, it iterates over all numbers from 2 to the square root of the length of the string, checking if the length is divisible by any of these numbers. If it is, the function returns false (since the length is not a prime number). If the function doesn't find any divisors, it returns true (since the length is a prime number). This solution has a time complexity of O(sqrt(n)), where n is the length of the string.