You can use the JavaScript `Math` object to achieve this. The `Math.floor()` function will return the largest integer less than or equal to a given number. Subtracting this from the original number will give you the decimal part. Here's the implementation:

```javascript
const truncateNumber = (number) => {
  return number - Math.floor(number);
}
```

In your example, calling `truncateNumber(3.5)` will return `0.5`.