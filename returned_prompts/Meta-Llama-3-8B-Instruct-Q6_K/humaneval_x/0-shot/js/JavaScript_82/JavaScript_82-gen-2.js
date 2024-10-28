Here is a JavaScript function that fulfills the requirements:

```javascript
const primeLength = (string) => {
  let length = string.length;
  if (length <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++) {
    if (length % i === 0) return false;
  }
  return true;
};
```

This function first calculates the length of the input string. Then it checks if the length is less than or equal to 1, in which case it returns `false` because 0 and 1 are not prime numbers. 

Then it iterates from 2 to the square root of the length, checking if the length is divisible by any of these numbers. If it is, the function returns `false` because the length is not a prime number. 

If the function finishes checking all the numbers without finding a divisor, it returns `true` because the length is a prime number. 

This function assumes that the input string is a non-empty string. If the input string can be an empty string or null, you should add checks for these cases at the beginning of the function. 

Here is how you can use this function:

```javascript
console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
``` 