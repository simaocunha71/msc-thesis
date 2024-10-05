Here is the solution using JavaScript:

```javascript
const uniqueDigits = (x) => {
  return x.filter(num => !hasEvenDigit(num)).sort((a, b) => a - b);
};

const hasEvenDigit = (num) => {
  return String(num).split('').some(digit => parseInt(digit) % 2 === 0);
};
```

The function `uniqueDigits` filters the input array `x` to include only the numbers that do not have any even digit. It does this by using the helper function `hasEvenDigit`, which checks if a given number has any even digit. It does this by converting the number to a string, splitting it into individual digits, and then checking if any of these digits is even. If the number has any even digit, the `hasEvenDigit` function returns `true`, and the `uniqueDigits` function filters it out. The remaining numbers are then sorted in increasing order and returned.

For example, if you call `uniqueDigits([15, 33, 1422, 1])`, the function will return `[1, 15, 33]`, which are the numbers that do not have any even digit. If you call `uniqueDigits([152, 323, 1422, 10])`, the function will return an empty array, because all the numbers in the input array have at least one even digit.