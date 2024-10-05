```javascript
const maxElement = (l) => {
  return Math.max(...l);
};
```
Explanation:
The `Math.max()` function returns the largest of a set of numbers. The `...` operator is used to spread the array into individual arguments to the `Math.max()` function. This allows the function to take an array of numbers and return the maximum value. 

For example, if we call `maxElement([1, 2, 3])`, it will return `3` which is the maximum element in the array. Similarly, if we call `maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])`, it will return `123` which is the maximum element in the array.