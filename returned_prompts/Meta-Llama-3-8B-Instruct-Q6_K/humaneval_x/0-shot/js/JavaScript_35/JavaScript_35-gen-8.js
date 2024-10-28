```javascript
const maxElement = (l) => Math.max(...l);
```
The problem asks to return the maximum element in a given list. We can use the built-in JavaScript function `Math.max()` and spread operator `...` to achieve this. The `Math.max()` function takes multiple arguments and returns the largest one. By using the spread operator, we can pass all the elements of the list as separate arguments to `Math.max()`.

Here's how it works:

- `Math.max()` is a function that returns the largest of the numbers given as arguments.
- The spread operator `...` is used to expand the array into separate arguments.
- When we pass `...l` as an argument to `Math.max()`, it treats each element of the array as a separate argument, and returns the maximum value.

For example, if we call `maxElement([1, 2, 3])`, it will return `3` because `3` is the maximum value in the array. If we call `maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])`, it will return `123` because `123` is the maximum value in the array.