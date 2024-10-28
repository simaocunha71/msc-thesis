```javascript
const changeBase = (x, base) => {
  let result = '';
  let remainder;

  while (x > 0) {
    remainder = x % base;
    result = remainder.toString() + result;
    x = Math.floor(x / base);
  }

  return result;
};
```


The function `changeBase` converts a number `x` to a different base `base`. It repeatedly divides the input number by the base, appends the remainder to the result, and updates the number. The process continues until the input number becomes 0. The result is the string representation of the number in the new base. The base numbers are less than 10, so we use the `toString()` method to convert the remainder to a string. The result is then prepended to the result string.

For example, if we call `changeBase(8, 3)`, the function will convert the number 8 to base 3, resulting in the string '22'. If we call `changeBase(8, 2)`, the function will convert the number 8 to base 2, resulting in the string '1000'. If we call `changeBase(7, 2)`, the function will convert the number 7 to base 2, resulting in the string '111'.