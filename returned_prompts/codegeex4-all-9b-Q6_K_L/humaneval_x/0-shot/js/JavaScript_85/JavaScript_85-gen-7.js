You can use the `filter` method to select the even numbers and the `reduce` method to sum them up. The `filter` method takes a callback function that returns `true` for even numbers, and the `reduce` method takes a callback function that adds the current number to the accumulator.

Here's the solution:

```javascript
const add = (lst) => {
  return lst.filter((num, i) => i % 2 !== 0 && num % 2 === 0).reduce((acc, num) => acc + num, 0);
};
```

In this solution, the `filter` method returns a new array that contains only the numbers that are at odd indices and are even. The `reduce` method then adds up these numbers and returns the sum. The second argument to `reduce` is the initial value of the accumulator, which is `0` in this case.