```javascript
const truncateNumber = (number) => {
  const intPart = Math.floor(number);
  return number - intPart;
};
```


In this solution, we use the `Math.floor()` function to get the integer part of the number. Then we subtract this integer part from the original number to get the decimal part. This works because `Math.floor()` returns the largest integer smaller than the given number, so the decimal part will always be the leftover part.