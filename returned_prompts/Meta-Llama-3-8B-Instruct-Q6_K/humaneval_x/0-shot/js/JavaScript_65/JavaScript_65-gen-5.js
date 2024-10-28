Here is the solution to the problem:
```
const circularShift = (x, shift) => {
  const str = x.toString();
  const len = str.length;
  shift = shift % len;
  return str.slice(shift) + str.slice(0, shift);
};
```
Explanation:

1. First, we convert the integer `x` to a string using the `toString()` method.
2. We calculate the length of the string using the `length` property.
3. We calculate the effective shift value by taking the remainder of the shift value modulo the length of the string. This is to handle the case where the shift value is greater than the number of digits.
4. We use the `slice()` method to extract two parts of the string: the part to be shifted to the end, and the part to be kept at the beginning.
5. We concatenate these two parts using the `+` operator to form the resulting string.

Testing:

```
console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"
```
This solution works by simply shifting the digits of the string representation of the integer, taking into account the effective shift value calculated in step 3. The `slice()` method is used to extract the parts of the string that need to be shifted, and the concatenation operator `+` is used to combine these parts into the resulting string.