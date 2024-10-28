```javascript
const greatestCommonDivisor = (a, b) => {
  // Make sure a is always greater than b
  if (a < b) {
    [a, b] = [b, a];
  }
  
  // Loop until b is 0
  while (b !== 0) {
    // Find remainder of a divided by b
    const remainder = a % b;
    
    // Update a and b for next iteration
    a = b;
    b = remainder;
  }
  
  // Return the greatest common divisor
  return a;
}
```
