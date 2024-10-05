  let num = parseFloat(value);
  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);
};

console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("14.5")); // 15
console.log(closestInteger("-14.5")); // -15

// Explanation:
// The function closestInteger first converts the input string into a number using parseFloat. It then rounds the number to the nearest integer by adding 0.5 to the number if it's positive or subtracting 0.5 if it's negative. This way, it effectively rounds the number away from zero when it's equidistant between two integers. Finally, it returns the rounded number using Math.floor.
// The test cases verify that the function works correctly.

```

## 2. Convert a number to a string with a specific number of decimals

```javascript
