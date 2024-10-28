  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  return isPrime(string.length);
};

console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false

// The function `primeLength` first defines a helper function `isPrime` that checks if a number is a prime number or not. It then returns the result of `isPrime` called with the length of the input string.

// `isPrime` iteratively checks if a number is divisible by any number up to its square root. If it is, the number is not prime and the function returns false. If it isn't, the function returns true. This is an efficient way to check for prime numbers as it only needs to check divisibility up to the square root of the number.

// Finally, `primeLength` returns the result of `isPrime` called with the length of the input string.

// Note: This function assumes that the input string is a non-empty string. If the string can be empty, the function should check for this case and return false if it is.

```

## Question 2:

```javascript
