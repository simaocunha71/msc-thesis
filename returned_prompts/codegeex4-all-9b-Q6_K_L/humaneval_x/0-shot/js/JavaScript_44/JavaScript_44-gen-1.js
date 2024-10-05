Here is the JavaScript code to solve the problem:

```javascript
const changeBase = (x, base) => {
  let result = '';
  while (x > 0) {
    result = (x % base) + result;
    x = Math.floor(x / base);
  }
  return result;
}
```
This function works by repeatedly dividing the number by the base and taking the remainder. The remainder is the next digit in the base representation of the number, and the quotient is the next number to be divided. The digits are then concatenated in reverse order to form the base representation of the number.