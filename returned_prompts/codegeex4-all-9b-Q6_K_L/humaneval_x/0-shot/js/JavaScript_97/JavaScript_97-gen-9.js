```js
const multiply = (a, b) => {
  return Math.abs(a % 10) * Math.abs(b % 10);
}
```
This solution uses the modulus operator (%) to get the last digit of each number, and then multiplies them together. The Math.abs() function is used to ensure that the result is always positive, regardless of the signs of the input numbers.