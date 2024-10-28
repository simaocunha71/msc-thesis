Here is a possible solution in JavaScript:
```
const circularShift = (x, shift) => {
  const str = x.toString();
  shift = shift % str.length; // adjust shift to be within the range of the number of digits
  return str.slice(shift) + str.slice(0, shift);
};
```
Here's an explanation of the code:

1. `x.toString()` converts the integer `x` to a string.
2. `shift % str.length` adjusts the shift to be within the range of the number of digits in the string. This is done to handle the case where `shift` is greater than the number of digits.
3. `str.slice(shift)` extracts the substring starting from the `shift`-th character to the end of the string.
4. `str.slice(0, shift)` extracts the substring from the beginning of the string to the `shift`-th character.
5. The two substrings are concatenated to form the result string.

You can test the function with the examples you provided:
```
console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"
```
I hope this helps! Let me know if you have any questions.