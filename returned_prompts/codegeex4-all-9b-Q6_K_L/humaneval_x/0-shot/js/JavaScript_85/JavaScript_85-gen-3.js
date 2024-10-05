You can use the `reduce` function to solve this problem. Here is a possible solution:

```javascript
const add = (lst) => {
  return lst.reduce((acc, curr, idx) => {
    if (idx % 2 !== 0 && curr % 2 === 0) {
      acc += curr;
    }
    return acc;
  }, 0);
}
```

In this solution, we iterate over the list using the `reduce` function. For each element, we check if the index is odd (`idx % 2 !== 0`) and if the element is even (`curr % 2 === 0`). If both conditions are true, we add the element to the accumulator (`acc`). Finally, we return the accumulator.