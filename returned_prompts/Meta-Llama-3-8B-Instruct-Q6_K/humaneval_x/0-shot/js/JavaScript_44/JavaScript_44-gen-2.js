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

console.log(changeBase(8, 3)); // '22'
console.log(changeBase(8, 2)); // '1000'
console.log(changeBase(7, 2)); // '111'
```


The function `changeBase` takes two parameters: `x` (the number to convert) and `base` (the base to convert to). It converts the number `x` to the base `base` and returns the string representation of the result.

Here's how it works:

1. It defines a string `digits` containing the digits 0-9.
2. It initializes an empty string `result` that will be used to store the converted number.
3. It enters a loop that continues as long as `x` is greater than 0.
4. Inside the loop, it calculates the remainder of `x` divided by `base` using the modulo operator (`%`). This gives the least significant digit of the converted number.
5. It prepends the calculated digit to the `result` string using concatenation (`+`).
6. It updates `x` by performing integer division of `x` by `base` using the `Math.floor` function. This effectively shifts the digits of the number to the right.
7. The loop continues until `x` is 0.
8. Finally, the function returns the `result` string.

The examples in the problem statement demonstrate the function's behavior with different inputs. For example, `changeBase(8, 3)` converts the decimal number 8 to the base 3 and returns the string `'22'`. Similarly, `changeBase(8, 2)` converts the decimal number 8 to the base 2 and returns the string `'1000'`.