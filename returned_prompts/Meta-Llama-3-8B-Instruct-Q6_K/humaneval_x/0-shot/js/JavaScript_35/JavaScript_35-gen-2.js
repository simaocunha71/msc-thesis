```
const maxElement = (l) => Math.max(...l);
```
Explanation:
The `Math.max()` function returns the maximum value in a list of numbers. The `...` operator is used to spread the array into separate arguments for the `Math.max()` function. This is a concise way to find the maximum value in an array. The function takes an array `l` as an argument and returns the maximum element in the array. For example, `maxElement([1, 2, 3])` returns `3` and `maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])` returns `123`.