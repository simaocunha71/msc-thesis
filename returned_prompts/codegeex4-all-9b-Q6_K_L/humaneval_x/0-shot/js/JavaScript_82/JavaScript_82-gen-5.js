```js
  const checkPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  };
  return checkPrime(string.length);
};
```
Explanation:
The `checkPrime` function checks if a number is prime by iterating from 2 to the number and checking if any of the numbers divide the given number evenly. If any number divides the given number evenly, it means the number is not prime and the function returns false. If no number divides the given number evenly, it means the number is prime and the function returns true. The `primeLength` function takes a string as input and returns true if the length of the string is prime or false otherwise.