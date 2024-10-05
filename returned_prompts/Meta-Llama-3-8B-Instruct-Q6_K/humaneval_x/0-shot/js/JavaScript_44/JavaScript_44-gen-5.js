Here is the solution for the problem:

```javascript
const changeBase = (x, base) => {
  const digits = '0123456789';
  let result = '';

  while (x > 0) {
    result = digits[x % base] + result;
    x = Math.floor(x / base);
  }

  return result;
};
```

In this solution, we define a function `changeBase` that takes two arguments: `x` (the number to be converted) and `base` (the base to which we want to convert `x`). We use a string `digits` to store the digits from 0 to 9, and an empty string `result` to store the result of the conversion.

We then use a while loop to repeatedly divide `x` by `base`, append the remainder to `result`, and update `x` to be the integer part of the division. This process continues until `x` becomes 0.

Finally, we return the string `result`, which represents the number `x` in the new base. For example, if we call `changeBase(8, 3)`, the function will return the string `'22'`, which is the binary representation of the octal number 8. If we call `changeBase(8, 2)`, the function will return the string `'1000'`, which is the binary representation of the octal number 8. If we call `changeBase(7, 2)`, the function will return the string `'111'`, which is the binary representation of the octal number 7.