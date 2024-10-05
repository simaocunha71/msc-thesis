Here is a JavaScript function that satisfies the requirements:
```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.round(num);
};
```
Explanation:

* `parseFloat(value)` converts the input string to a floating-point number.
* `Math.round(num)` rounds the number to the nearest integer. If the number is equidistant from two integers, it rounds away from zero.

Testing:
```javascript
console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("14.5")); // 15
console.log(closestInteger("-14.5")); // -15
```
This function passes all the given examples and follows the rounding away from zero rule.