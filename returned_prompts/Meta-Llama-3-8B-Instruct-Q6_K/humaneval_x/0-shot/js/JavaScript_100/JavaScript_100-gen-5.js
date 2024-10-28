Here is the solution to the problem:
```
const makeAPile = (n) => {
  const pile = [];
  let level = n;

  for (let i = 0; i < n; i++) {
    pile.push(level);
    if (level % 2 === 0) {
      level += 1;
    } else {
      level += 2;
    }
  }

  return pile;
};
```
Explanation:

The function `makeAPile` takes an integer `n` as input and returns a list of integers representing the number of stones in each level of the pile.

The function initializes an empty list `pile` and a variable `level` set to `n`. It then enters a loop that runs `n` times.

In each iteration of the loop, the function adds the current `level` to the `pile` list and updates the `level` variable based on whether the previous level had an odd or even number of stones. If the previous level had an odd number of stones, the next level will have an even number of stones (i.e., `level` is incremented by 2). If the previous level had an even number of stones, the next level will have an odd number of stones (i.e., `level` is incremented by 1).

Finally, the function returns the `pile` list, which contains the number of stones in each level of the pile. For example, if `n` is 3, the function will return the list `[3, 5, 7]`, representing the number of stones in each level of the pile.