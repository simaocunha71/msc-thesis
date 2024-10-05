```javascript
const truncateNumber = (number) => {
  return number - Math.floor(number);
}
```
Explanation:
The function `truncateNumber` takes a positive floating point number as an argument. It returns the decimal part of the number. The decimal part is obtained by subtracting the integer part from the number. The integer part is obtained by using the `Math.floor` function, which returns the largest integer smaller than or equal to the given number. Therefore, the decimal part is the difference between the original number and the integer part. This is achieved by `number - Math.floor(number)`. For example, if the input is `3.5`, `Math.floor(3.5)` returns `3`, so `3.5 - 3 = 0.5`, which is the decimal part. This is the expected output.