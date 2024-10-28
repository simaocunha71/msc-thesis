Here is a JavaScript solution for the problem:

```javascript
const sumSquares = (lst) => {
  return lst.map(x => Math.ceil(x)**2).reduce((a, b) => a + b, 0);
};
```

Explanation:
The `map` method is used to apply the `Math.ceil` function to each element in the list, effectively rounding each number up to the nearest integer. The `**` operator is used to square each number. The `reduce` method is used to sum up the squared numbers. The initial value of the accumulator is set to `0`, so the sum starts from `0`. The `map` and `reduce` methods return a new array and a number respectively, which is the sum of the squared numbers. The result is then returned by the `sumSquares` function.

For example, if you call `sumSquares([1,2,3])`, the function will return `14`, which is the sum of the squared numbers `1**2`, `2**2`, and `3**2`, where each number is rounded up to the nearest integer.