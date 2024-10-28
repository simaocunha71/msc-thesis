```javascript
const maxElement = (l) => Math.max(...l);
```
Explanation:
The `Math.max()` function returns the largest of the given numbers. In this case, we use the spread operator (`...`) to pass the elements of the array `l` as separate arguments to `Math.max()`. This allows us to find the maximum element in the array. The `Math.max()` function then returns the largest number, which is the maximum element in the list.