```javascript
function truncateNumber(number) {
  const integerPart = Math.floor(number);
  return number - integerPart;
}

console.log(truncateNumber(3.5)); // 0.5
```


This solution works by first using the `Math.floor()` function to get the largest integer smaller than the given number. Then, it subtracts this integer part from the original number to get the decimal part. This decimal part is the desired output. The `Math.floor()` function is used to get the largest integer smaller than the given number, which is the integer part of the number. This function works by rounding down to the nearest integer. For example, `Math.floor(3.5)` returns `3`, and `Math.floor(3.9)` also returns `3`. So, subtracting the integer part from the original number gives the decimal part. For example, `3.5 - 3` gives `0.5`. This is the solution to the problem.