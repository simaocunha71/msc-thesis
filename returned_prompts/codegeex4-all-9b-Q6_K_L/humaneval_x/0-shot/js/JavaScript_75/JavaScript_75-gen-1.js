You can solve this problem by using the following steps:

1. Create a helper function to check if a number is a prime number.
2. Create a helper function to check if a number is a multiplication of 3 prime numbers.
3. Use the helper function to check if the given number is a multiplication of 3 prime numbers.

Here's the code:

```javascript
const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const isMultiplyPrime = (a) => {
  if (a < 2) return false;
  let count = 0;
  for (let i = 2; i <= a; i++) {
    if (isPrime(i) && a % i === 0) {
      count++;
    }
  }
  return count === 3;
};

console.log(isMultiplyPrime(30)); // true
```

The `isPrime` function checks if a number is a prime number by iterating from 2 to the square root of the number and checking if the number is divisible by any of the numbers in the range.

The `isMultiplyPrime` function checks if a number is a multiplication of 3 prime numbers by iterating from 2 to the number and checking if each number is a prime number and a factor of the number. If the count of prime factors is equal to 3, then the number is a multiplication of 3 prime numbers.

Note that the `isMultiplyPrime` function assumes that the given number is greater than or equal to 2. If the given number is less than 2, it returns false.