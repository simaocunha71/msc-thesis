  if (n <= 1) return false;
  if (n <= 3) return true;

  if (n % 2 === 0 || n % 3 === 0) return false;

  for (let i = 5; i * i <= n; i = i + 6) {
    if (n % i === 0 || n % (i + 2) === 0) return false;
  }

  return true;
};

module.exports = isPrime;








*/

Answer:

Here's a function that checks if a given number is prime or not:

```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  if (n <= 3) return true;

  if (n % 2 === 0 || n % 3 === 0) return false;

  for (let i = 5; i * i <= n; i = i + 6) {
    if (n % i === 0 || n % (i + 2) === 0) return false;
  }

  return true;
};
```

To use the function, you can simply call it with the number you want to check as an argument. For example, if you want to check if the number 6 is prime, you can do:

```javascript
console.log(isPrime(6)); // false
```

The function will return `true` if the number is prime, and `false` otherwise. The function works by checking if the number is divisible by any prime numbers less than or equal to its square root. If it is divisible by any of these numbers, it is not prime. Otherwise, it is prime.

Here are some example usages of the function:

```javascript
console.log(isPrime(101)); // true
console.log(isPrime(11)); // true
console.log(isPrime(13441)); // true
console.log(isPrime(61)); // true
console.log(isPrime(4)); // false
console.log(isPrime(1