You can solve this problem using the built-in JavaScript `Math.max()` function. Here's how you can do it:

```javascript
const maxElement = (l) => {
  return Math.max(...l);
};
```

This function takes an array `l` as an argument and returns the maximum element in the array. The `Math.max()` function takes an unlimited number of arguments, and the spread operator `...` is used to pass the elements of the array as separate arguments to `Math.max()`. For example, if the input array is `[1, 2, 3]`, `Math.max(...[1, 2, 3])` is equivalent to `Math.max(1, 2, 3)`, which returns `3`. 

So, if you call `maxElement([1, 2, 3])`, it will return `3`. If you call `maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])`, it will return `123`. 

This solution has a time complexity of O(1) and a space complexity of O(1), because it only requires a constant amount of space to store the function and the input array, and it only requires a constant amount of time to execute, regardless of the size of the input array. 