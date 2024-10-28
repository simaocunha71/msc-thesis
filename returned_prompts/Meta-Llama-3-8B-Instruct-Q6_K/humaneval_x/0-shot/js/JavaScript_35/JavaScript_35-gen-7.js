```javascript
const maxElement = (l) => {
  return Math.max(...l);
};
```


This solution uses the `Math.max()` function and the spread operator (`...`) to find the maximum element in the list. The `Math.max()` function takes a variable number of arguments and returns the largest one. The spread operator (`...`) is used to expand the list into separate arguments for the `Math.max()` function. For example, if the list is `[1, 2, 3]`, the spread operator expands it into `Math.max(1, 2, 3)`, which returns `3`. This solution works for lists of any length and returns the maximum element.