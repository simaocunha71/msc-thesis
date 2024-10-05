The task is to create a function that takes a string representing a number and returns the closest integer to it. If the number is equidistant from two integers, the function should round it away from zero. To achieve this, we can use the `Math.round` function, which rounds a number to the nearest integer. For positive numbers, this function rounds towards infinity, and for negative numbers, it rounds towards negative infinity. This behavior aligns with the requirement to round away from zero.

Here's the complete function:

```javascript
const closestInteger = (value) => {
  // Convert the string to a number
  const num = parseFloat(value);
  // Round the number to the nearest integer
  const rounded = Math.round(num);
  // Return the rounded number
  return rounded;
};

// Examples
console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("14.5")); // 15
console.log(closestInteger("-14.5")); // -15
```

This function first converts the input string to a floating-point number using `parseFloat`. It then rounds this number to the nearest integer using `Math.round`. Finally, it returns the rounded number. The examples provided demonstrate how the function behaves for various inputs.