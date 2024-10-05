```javascript
const maxElement = (l) => {
  return Math.max(...l);
};
```


Explanation:
The problem asks you to write a function that returns the maximum element in a given list. You can use the built-in JavaScript function `Math.max()` to achieve this. The `Math.max()` function takes a variable number of arguments and returns the maximum of those arguments.

In this case, we can use the spread operator `...` to pass the elements of the list as separate arguments to `Math.max()`. This allows us to find the maximum element in the list in a concise and efficient way.

For example, if you call `maxElement([1, 2, 3])`, the function will return `3`, which is the maximum element in the list. Similarly, if you call `maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])`, the function will return `123`, which is the maximum element in the list.