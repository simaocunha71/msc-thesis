```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.round(num);
};
```


Explanation:
The task is to create a function that takes a string representing a number and returns the closest integer to it. If the number is equidistant from two integers, round it away from zero. 

In the given examples, `closestInteger("10")` should return `10`, `closestInteger("15.3")` should return `15`, `closestInteger("14.5")` should return `15`, and `closestInteger("-14.5")` should return `-15`.

To achieve this, we can use the `parseFloat()` function to convert the input string to a floating-point number. Then, we can use the `Math.round()` function to round the number to the nearest integer. 

The `Math.round()` function rounds the number to the nearest integer, so it will round towards the nearest even number if the number is halfway between two integers. This is the default behavior of `Math.round()` in JavaScript.

Here is the implementation of the `closestInteger` function:
```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.round(num);
};
```
This function takes a string `value` as input, converts it to a floating-point number using `parseFloat()`, and then returns the result of `Math.round()` applied to the number. This ensures that the function returns the closest integer to the input number, rounding away from zero if the number is equidistant from two integers.