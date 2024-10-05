You can use the `Math.trunc()` method to truncate the decimal part of the number. Here's the solution:

```javascript
const truncateNumber = (number) => {
  return number - Math.trunc(number);
}
```

In this code, `Math.trunc(number)` will return the integer part of the number, and subtracting it from the original number will give us the decimal part.