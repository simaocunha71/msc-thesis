```javascript
const circularShift = (x, shift) => {
  // Convert the number to a string
  let xStr = x.toString();

  // If shift is greater than the number of digits, return the digits reversed
  if (shift > xStr.length) {
    return xStr.split('').reverse().join('');
  }

  // Perform the circular shift
  let shiftedStr = xStr.slice(-shift) + xStr.slice(0, -shift);

  return shiftedStr;
}
```
