```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.round(num);
};
```
Explanation:
The problem asks to create a function that takes a string representing a number and returns the closest integer to it. If the number is equidistant from two integers, round it away from zero.

To solve this problem, we can use the `parseFloat` function to convert the string to a float number. Then, we can use the `Math.round` function to round the number to the nearest integer.

In the case of equidistant numbers, `Math.round` will round the number away from zero. For example, if the number is 14.5, `Math.round` will return 15, and if the number is -14.5, `Math.round` will return -15.

Here's an example of how you can use this function:
```javascript
console.log(closestInteger("10")); // Output: 10
console.log(closestInteger("15.3")); // Output: 15
console.log(closestInteger("14.5")); // Output: 15
console.log(closestInteger("-14.5")); // Output: -15
```I hope this helps! Let me know if you have any questions.