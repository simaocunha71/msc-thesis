You can solve this problem by using the built-in `Math.round()` function. This function rounds a number to the nearest integer. If the number is equidistant from two integers, it rounds to the one that is the farthest from zero.

Here's how you can implement the `closestInteger` function:

```javascript
const closestInteger = (value) => {
  // Parse the value to a number
  const num = parseFloat(value);

  // Round the number and return the result
  return Math.round(num);
};
```

You can test the function with the provided examples:

```javascript
console.log(closestInteger("10"));  // Output: 10
console.log(closestInteger("15.3"));  // Output: 15
```

This solution assumes that the input value is always a string that can be converted to a number. If you want to handle edge cases or errors, you can add additional validation and error handling logic.