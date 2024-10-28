To solve this problem, we can follow these steps:

1. Convert the integer x to a string.
2. Check if the shift is greater than the number of digits in x. If it is, reverse the string and return it.
3. If the shift is not greater than the number of digits, perform the circular shift by slicing the string at the shift position and concatenating it with the remaining part of the string.
4. Return the resulting string.

Here is the implementation of the circularShift function in JavaScript:

```javascript
const circularShift = (x, shift) => {
  const str = x.toString();
  const numDigits = str.length;

  if (shift > numDigits) {
    return str.split('').reverse().join('');
  } else {
    return str.slice(shift) + str.slice(0, shift);
  }
};
```

Let's test the function with the provided examples:

```javascript
console.log(circularShift(12, 1)); // Output: "21"
console.log(circularShift(12, 2)); // Output: "12"
```

Both examples return the expected outputs.