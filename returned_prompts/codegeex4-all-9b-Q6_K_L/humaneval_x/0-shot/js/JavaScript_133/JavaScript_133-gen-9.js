You can use the `map()` function to round each element in the list to the ceiling, then use the `reduce()` function to sum the squares of the rounded numbers. Here's how you can do it:

```javascript
const sumSquares = (lst) => {
  return lst.map(Math.ceil).reduce((a, b) => a + b ** 2, 0);
};
```

Explanation:

- `Math.ceil()` is a built-in JavaScript function that rounds a number up to the nearest integer.
- `lst.map(Math.ceil)` will create a new array where each element is the ceiling of the corresponding element in `lst`.
- `reduce()` is a built-in JavaScript function that reduces an array to a single value by applying a function to each element in the array.
- `(a, b) => a + b ** 2` is an arrow function that takes two arguments `a` and `b` and returns their sum. In this case, `a` is the running total and `b` is the current element in the array. `b ** 2` is `b` squared.
- `0` is the initial value of the running total.