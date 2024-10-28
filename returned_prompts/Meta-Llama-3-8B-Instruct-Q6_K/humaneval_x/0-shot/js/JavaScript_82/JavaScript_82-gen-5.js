Here is the solution using JavaScript:

```javascript
const primeLength = (string) => {
  const length = string.length;
  if (length <= 1) return false;
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) return false;
  }
  return true;
};
```
This function works by first checking if the length of the string is less than or equal to 1, in which case it returns false because prime numbers are greater than 1. Then it checks if the length is divisible by any number from 2 to the square root of the length. If it finds a divisor, it returns false. If it doesn't find any divisors, it returns true, indicating that the length is a prime number. 