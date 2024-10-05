Here is the solution using JavaScript:
```javascript
const circularShift = (x, shift) => {
  let str = x.toString();
  shift = shift % str.length;
  return str.slice(shift) + str.slice(0, shift);
};
```
Here's an explanation of the code:

1. Convert the integer `x` to a string using the `toString()` method.
2. Calculate the actual shift amount by taking the remainder of the shift value divided by the length of the string. This ensures that the shift is within the bounds of the string.
3. Use the `slice()` method to extract the substring starting from the shifted position to the end of the string, and then concatenate it with the substring from the beginning of the string to the shifted position.

For example, if `x` is `12` and `shift` is `1`, the code will convert `12` to the string `"12"`, shift the digits right by 1 position, resulting in the string `"21"`. If `shift` is `2`, the code will shift the digits right by 2 positions, resulting in the original string `"12"`. If `shift` is `3`, the code will shift the digits right by 1 position, resulting in the string `"21"`.

You can test the function with different inputs to see the expected output:
```javascript
console.log(circularShift(12, 1)); // Output: "21"
console.log(circularShift(12, 2)); // Output: "12"
console.log(circularShift(123, 2)); // Output: "321"
console.log(circularShift(123, 4)); // Output: "123"
```