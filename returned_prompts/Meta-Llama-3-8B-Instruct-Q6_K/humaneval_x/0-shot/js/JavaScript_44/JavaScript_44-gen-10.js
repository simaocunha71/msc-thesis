Here is the solution to the problem:

```javascript
const changeBase = (x, base) => {
  let result = '';
  let remainder;
  let temp = x;

  while (temp > 0) {
    remainder = temp % base;
    temp = Math.floor(temp / base);
    if (remainder < 10) {
      result = remainder.toString() + result;
    } else {
      result = String.fromCharCode(55 + remainder) + result; // ASCII values for 'A' to 'F'
    }
  }
  return result;
};

// Testing the function
console.log(changeBase(8, 3)); // '22'
console.log(changeBase(8, 2)); // '1000'
console.log(changeBase(7, 2)); // '111'
```

This function works by repeatedly dividing the input number by the base and appending the remainder to the result string. The remainder is converted to a character if it's greater than 9 (to represent the digits 'A' to 'F' in hexadecimal), otherwise it's converted to a string. The process continues until the input number becomes 0. The final result is the string representation of the input number in the desired base.