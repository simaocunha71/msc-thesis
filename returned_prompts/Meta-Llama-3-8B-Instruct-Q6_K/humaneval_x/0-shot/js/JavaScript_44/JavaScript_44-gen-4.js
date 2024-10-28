Here is a possible solution:
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
This function uses a while loop to repeatedly divide the input number `x` by the base and append the remainder to the result string. The remainder is obtained using the modulo operator (`x % base`), and the result is prepended to the string using the concatenation operator (`+`).

For example, if we call `changeBase(8, 3)`, the function will iterate as follows:

* `x = 8`, `result = ''`, `base = 3`
* `x % 3 = 2`, `result = '2'`, `x = 2`
* `x % 3 = 2`, `result = '22'`, `x = 0`
* `x = 0`, `result = '22'`

The final result is `'22'`, which is the string representation of the number 8 in base 3.

Note that this function assumes that the input base is a positive integer less than 10. If the input base is not in this range, the function may produce incorrect results. You may want to add input validation to handle this case.