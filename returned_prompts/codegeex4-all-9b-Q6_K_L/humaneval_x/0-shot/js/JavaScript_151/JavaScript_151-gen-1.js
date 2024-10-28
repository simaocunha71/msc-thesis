You can solve this problem by using the `reduce` function. Here is a possible solution:

```javascript
const doubleTheDifference = (lst) => {
  return lst
    .filter((num) => num % 2 !== 0 && num > 0 && Number.isInteger(num))
    .reduce((acc, curr) => acc + curr * curr, 0);
};
```

In this solution, we first filter the list to keep only the numbers that are odd, positive, and integers. Then, we use the `reduce` function to calculate the sum of squares of the remaining numbers. If the list is empty, the `reduce` function will return `0` by default.