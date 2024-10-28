To solve this problem, we need to first create a helper function to check if a number is prime or not. Then, we can use this helper function to check if the length of the given string is prime or not.

Here is the solution:

```javascript
const primeLength = (string) => {
  const isPrime = (num) => {
    if (num < 2) {
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

In this solution, the `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if any of the numbers divide the given number evenly. If any number divides the given number evenly, the function returns false, indicating that the number is not prime. If none of the numbers divide the given number evenly, the function returns true, indicating that the number is prime.

The `primeLength` function then simply calls the `isPrime` function with the length of the given string and returns the result.