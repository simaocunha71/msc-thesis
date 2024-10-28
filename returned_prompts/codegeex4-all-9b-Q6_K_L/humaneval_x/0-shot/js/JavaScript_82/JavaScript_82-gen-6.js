You can create a helper function `isPrime` to check if a number is prime. Then, use this function in your `primeLength` function to return whether the length of the string is prime or not. Here is an example implementation:

```javascript
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const primeLength = (string) => {
  return isPrime(string.length);
};
```

You can now call the `primeLength` function to check if the length of a string is a prime number.