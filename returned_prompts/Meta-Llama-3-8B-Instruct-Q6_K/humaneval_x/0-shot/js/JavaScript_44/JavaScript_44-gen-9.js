Here is the solution in JavaScript:
```javascript
const changeBase = (x, base) => {
  const digits = '0123456789';
  const result = [];
  while (x > 0) {
    result.unshift(digits[x % base]);
    x = Math.floor(x / base);
  }
  return result.join('');
};
```
Here's an explanation of the code:

1. We define the `changeBase` function that takes two arguments: `x` (the input number) and `base` (the target base).
2. We define a string `digits` that contains the digits from 0 to 9.
3. We create an empty array `result` to store the digits of the input number in the target base.
4. We use a while loop to repeatedly divide the input number `x` by the target base `base`, and append the remainder to the `result` array using `unshift`.
5. Finally, we join the elements of the `result` array into a single string using `join('')`, and return the resulting string.

