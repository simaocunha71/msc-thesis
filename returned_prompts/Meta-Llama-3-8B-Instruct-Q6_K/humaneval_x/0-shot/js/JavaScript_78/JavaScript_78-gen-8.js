Here is a JavaScript function that solves the problem:

```javascript
const hexKey = (num) => {
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let hexDigit = num[i];
    let decimalValue;
    switch (hexDigit) {
      case '2':
      case '3':
      case '5':
      case '7':
      case 'B':
      case 'D':
        decimalValue = parseInt(hexDigit, 16);
        if (isPrime(decimalValue)) {
          count++;
        }
    }
  }
  return count;
};

const isPrime = (n) => {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};
```

In this function, we first iterate over each character in the input string. If the character is '2', '3', '5', '7', 'B', or 'D', we convert it to its decimal value and check if it's a prime number using the `isPrime` function. If it is, we increment the count. Finally, we return the count.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it's not a prime number, so we return false. If we reach the end of the loop without finding a divisor, we return true.