To determine if the length of a string is a prime number, you can create a helper function that checks if a number is prime. Then, you can use this helper function to check the length of the string. Here's how you can do it:

```javascript
const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const primeLength = (string) => {
  return isPrime(string.length);
};
```

Let's test the function with the provided examples:

```javascript
console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
```

The output will be:

```
true
true
true
false
```

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is divisible, it's not a prime number, and the function returns `false`. Otherwise, it returns `true`.