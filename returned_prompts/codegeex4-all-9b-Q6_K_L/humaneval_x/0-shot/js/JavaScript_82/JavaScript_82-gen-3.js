To solve this problem, we need to create a function that checks if a number is prime or not. Then, we can use this function to check if the length of the given string is a prime number. Here is the complete solution:

```javascript
const primeLength = (string) => {
  const isPrime = (num) => {
    if (num <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  };
  return isPrime(string.length);
};
```

Explanation:
1. We create a helper function called `isPrime` that takes a number as an argument and checks if it is a prime number or not.
2. Inside `isPrime`, we first check if the number is less than or equal to 1. If it is, we return `false` because 1 and numbers less than 1 are not prime.
3. Next, we loop from 2 to the square root of the given number. We check if the given number is divisible by any number in this range. If it is, we return `false` because it is not a prime number.
4. If the given number is not divisible by any number in the range, we return `true` because it is a prime number.
5. Finally, we call the `isPrime` function with the length of the given string and return the result.