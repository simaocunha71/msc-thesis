Here is the solution using JavaScript:

```javascript
const circularShift = (x, shift) => {
  x = Math.abs(x).toString();
  shift = shift % x.length;
  if (shift === 0) return x;
  return x.slice(shift) + x.slice(0, shift);
};
```

Explanation:

*   We convert the integer `x` to a string using `Math.abs(x).toString()`.
*   We calculate the shift value by taking the modulus of `shift` with the length of the string `x`. This is to handle cases where `shift` is greater than the number of digits in `x`.
*   If `shift` is 0, we simply return the original string `x`.
*   Otherwise, we use the `slice` method to extract the substring from `shift` to the end of the string and concatenate it with the substring from the beginning of the string to `shift`. This effectively performs a circular shift of the digits.