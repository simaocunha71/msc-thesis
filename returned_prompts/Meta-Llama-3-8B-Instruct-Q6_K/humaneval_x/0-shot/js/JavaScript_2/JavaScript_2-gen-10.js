```javascript
function truncateNumber(number) {
  const integerPart = Math.floor(number);
  return number - integerPart;
}
```
Explanation:
The function `truncateNumber` takes a positive floating point number as an argument. It uses the `Math.floor` function to get the integer part of the number. The integer part is the largest integer smaller than the given number. The decimal part is calculated by subtracting the integer part from the original number.

For example, for the input `3.5`, the integer part is `3` and the decimal part is `0.5`. The function returns `0.5` which is the decimal part of the number.