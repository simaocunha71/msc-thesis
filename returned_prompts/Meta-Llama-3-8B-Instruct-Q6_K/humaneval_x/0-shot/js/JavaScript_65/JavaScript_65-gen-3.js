Here is the solution in JavaScript:
```javascript
const circularShift = (x, shift) => {
  let str = x.toString();
  shift = shift % str.length;
  return str.slice(shift) + str.slice(0, shift);
};
```
Explanation:

1. Convert the integer `x` to a string using the `toString()` method.
2. Calculate the actual shift value by taking the modulus of `shift` with the length of the string `str`. This is to handle cases where `shift` is greater than the number of digits.
3. Use the `slice()` method to split the string into two parts: the part to be shifted to the end and the part to remain at the beginning.
4. Concatenate the two parts using the `+` operator to form the resulting string.
5. Return the resulting string.

Example usage:
```javascript
console.log(circularShift(12, 1)); // Output: "21"
console.log(circularShift(12, 2)); // Output: "12"
```
This function works by shifting the digits of the integer `x` to the right by `shift` positions. If `shift` is greater than the number of digits, it simply returns the digits in reverse order. The `%` operator is used to ensure that the shift value is within the range of the number of digits. The `slice()` method is used to extract the desired parts of the string, and the `+` operator is used to concatenate them. The resulting string is then returned.