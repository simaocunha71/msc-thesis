```
const sumSquares = (lst) => {
  return lst.map(num => Math.ceil(num) ** 2).reduce((a, b) => a + b, 0);
};
```


Explanation:

*   We use the `map()` function to apply a transformation to each element in the list. In this case, we use `Math.ceil(num)` to round each number up to the nearest integer.
*   We use the `reduce()` function to calculate the sum of the squared numbers. The initial value of the accumulator is set to `0`.
*   The callback function `(a, b) => a + b` adds the current sum `a` and the current squared number `b` to get the new sum.
*   Finally, we return the calculated sum.