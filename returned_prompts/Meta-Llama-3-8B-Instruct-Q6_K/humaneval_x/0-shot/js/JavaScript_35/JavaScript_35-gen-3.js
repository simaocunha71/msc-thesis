```javascript
const maxElement = (l) => Math.max(...l);
```
This function uses the `Math.max()` function with the spread operator (`...`) to find the maximum element in the list. The `Math.max()` function takes a variable number of arguments, so by using the spread operator, we can pass the entire list to it and it will return the maximum value. For example, if the list is `[1, 2, 3]`, `Math.max(1, 2, 3)` would return `3`. If the list is `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`, `Math.max(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)` would return `123`. This function will work with any list of numbers, not just the ones provided in the problem description. It also works with lists of negative numbers, or lists with a mix of positive and negative numbers. It even works with lists that contain only one element, in which case it simply returns that element. It also works with lists that are empty, in which case it returns `NaN` (Not a Number). This is because `Math.max()` returns `NaN` when given no arguments. If you want to handle the case where the list is empty, you could add a check at the beginning of the function:
```javascript
const maxElement = (l) => {
  if (l.length === 0) return null; // or some other value to indicate an empty list
  return Math.max(...l);
};
```
This way, if the list is empty, the function will return `null` instead of `NaN`. You could also return an error message or throw an error, depending on your needs.