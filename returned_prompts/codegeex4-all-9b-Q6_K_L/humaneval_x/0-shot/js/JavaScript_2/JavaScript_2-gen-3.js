You can use the `Math.trunc()` method to truncate the decimal part of the number and then subtract the result from the original number to get the decimal part.

Here's the solution:

```javascript
const truncateNumber = (number) => {
  const integerPart = Math.trunc(number);
  return number - integerPart;
}
```

This code first calculates the integer part of the number using `Math.trunc()`, which truncates the decimal part. Then it subtracts the integer part from the original number to get the decimal part.