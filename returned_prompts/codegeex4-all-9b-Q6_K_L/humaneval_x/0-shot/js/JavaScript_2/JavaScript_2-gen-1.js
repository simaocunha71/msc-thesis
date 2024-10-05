The question is asking to return the decimal part of a given number. To achieve this we can subtract the integer part of the number from the original number. The `Math.floor()` function will return the largest integer smaller than the given number which we can subtract from the original number to get the decimal part.

Here is the solution:

```javascript
const truncateNumber = (number) => {
  return number - Math.floor(number);
}
```

This will return the decimal part of the number.

Example:
```javascript
console.log(truncateNumber(3.5));  // Output: 0.5
console.log(truncateNumber(10.7));  // Output: 0.7
console.log(truncateNumber(0.2));  // Output: 0.2
```