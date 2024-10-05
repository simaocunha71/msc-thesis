To get the decimal part of a number in JavaScript, you can subtract the integer part from the original number. Here's how you can do it:

```javascript
const truncateNumber = (number) => {
  const integerPart = Math.floor(number);
  return number - integerPart;
};
```

This code first uses the `Math.floor()` function to get the largest integer smaller than the given number. Then, it subtracts this integer part from the original number to get the decimal part.