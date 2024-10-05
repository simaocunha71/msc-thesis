You can solve this problem using JavaScript's array methods like `filter()`, `map()`, and `reduce()`. Here's a solution:

```javascript
const solution = (lst) => {
  return lst.filter((num, index) => index % 2 === 0 && num % 2 !== 0)
    .reduce((acc, curr) => acc + curr, 0);
}
```

In this solution, `filter()` is used to select only the odd numbers that are in even positions, then `reduce()` is used to sum up the selected numbers. The `reduce()` function takes two arguments: the accumulator (`acc`) and the current value (`curr`). It returns the sum of these two values, which is then used as the accumulator for the next iteration. The second argument to `reduce()` is the initial value of the accumulator, which is `0`.