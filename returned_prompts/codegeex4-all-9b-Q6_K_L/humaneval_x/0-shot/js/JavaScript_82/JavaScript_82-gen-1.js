Here is the JavaScript code to solve the problem:

```javascript
const primeLength = (string) => {
  let length = string.length;

  // Check if the length is less than 2
  if(length < 2) {
    return false;
  }

  // Loop through 2 to length/2
  for(let i = 2; i <= Math.floor(length / 2); i++) {
    // If length is divisible by i, then it's not a prime number
    if(length % i === 0) {
      return false;
    }
  }

  // If none of the numbers divided the length, it's a prime number
  return true;
};
```

You can test the function with the following code:

```javascript
console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
```