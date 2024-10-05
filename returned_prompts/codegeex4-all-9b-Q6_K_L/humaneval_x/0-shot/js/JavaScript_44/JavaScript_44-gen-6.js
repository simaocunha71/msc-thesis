Here's how you could write the `changeBase` function in JavaScript:

```javascript
const changeBase = (x, base) => {
  let result = '';
  while (x > 0) {
    result = (x % base) + result;
    x = Math.floor(x / base);
  }
  return result;
};
```

This function works by repeatedly dividing the number `x` by `base`, and prepending the remainder to the result string. It continues this process until `x` is 0. The `Math.floor` function is used to ensure that the division is truncated down to the nearest integer, which is necessary for correct base conversion.

You can test this function with the following code:

```javascript
console.log(changeBase(8, 3)); // '22'
console.log(changeBase(8, 2)); // '1000'
console.log(changeBase(7, 2)); // '111'
```

This should produce the expected output for the given test cases.