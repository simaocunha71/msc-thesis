```javascript
const generateIntegers = (a, b) => {
  // Determine the lower and upper bounds
  const lower = Math.min(a, b);
  const upper = Math.max(a, b);

  // Initialize the result array
  const result = [];

  // Iterate through the range of numbers
  for (let i = lower; i <= upper; i++) {
    // Convert the number to a string
    const str = i.toString();

    // Check if all digits are even
    const isEven = str.split('').every(digit => digit % 2 === 0);

    // If all digits are even, add the number to the result array
    if (isEven) {
      result.push(i);
    }
  }

  // Return the result array
  return result;
};
```