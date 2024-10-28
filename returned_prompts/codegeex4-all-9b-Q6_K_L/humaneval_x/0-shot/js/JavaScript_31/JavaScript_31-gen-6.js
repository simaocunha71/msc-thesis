To determine if a number \( n \) is prime, you need to check if it has any divisors other than 1 and itself. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

Here's the code to implement the `isPrime` function:

```javascript
const isPrime = (n) => {
  // Check if n is less than 2 (not prime)
  if (n < 2) {
    return false;
  }

  // Check if n is 2 (prime)
  if (n === 2) {
    return true;
  }

  // Check if n is even (not prime)
  if (n % 2 === 0) {
    return false;
  }

  // Check for odd factors
  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    if (n % i === 0) {
      return false;
    }
  }

  return true;
};
```

### Explanation:
1. **Check for numbers less than 2**: Any number less than 2 is not prime.
2. **Check for 2**: 2 is the only even prime number.
3. **Check for even numbers**: If \( n \) is greater than 2 and is even, it's not prime.
4. **Check for odd factors**: Iterate from 3 to the square root of \( n \), checking if \( n \) is divisible by any odd number. If it is, it's not prime.
5. **Return true**: If none of the above conditions are met, \( n \) is prime, so return true.

This function efficiently checks if a number is prime by reducing the number of checks needed. It only checks up to the square root of \( n \) because if \( n \) has a factor greater than its square root, it must also have a factor smaller than its square root.