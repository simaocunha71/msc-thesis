  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  return isPrime(string.length);
}
console.log(primeLength('Hello')) // true
console.log(primeLength('abcdcba')) // true
console.log(primeLength('kittens')) // true
console.log(primeLength('orange')) // false

```

This function isPrime checks if a given number is a prime number or not. If the string length is a prime number, it returns true; otherwise, it returns false.

Explanation of the code:

- The function isPrime checks if a number is a prime number or not.
- A number is considered prime if it is greater than 1 and has no divisors other than 1 and itself.
- For a given number, we only need to check divisors up to the square root of that number.
- If the number is divisible by any number up to its square root, it is not a prime number.
- If the number is greater than 1 and not divisible by any number up to its square root, it is a prime number.
- The function isPrime is called with the length of the string as an argument.
- If the length of the string is a prime number, the function primeLength returns true; otherwise, it returns false.
- The function primeLength is then tested with the strings 'Hello', 'abcdcba', 'kittens', and 'orange'.
- The results are logged to the console.
*/

```

## 12. Is Palindrome

```javascript
