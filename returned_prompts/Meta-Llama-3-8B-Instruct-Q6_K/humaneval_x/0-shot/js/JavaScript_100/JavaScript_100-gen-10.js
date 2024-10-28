Here is the solution for the problem:
```
const makeAPile = (n) => {
  const result = [];
  let level = 1;
  let stones = n;

  while (stones > 0) {
    result.push(stones);
    stones = level % 2 === 0 ? level + 1 : level + 2;
    level++;
  }

  return result;
};
```
Explanation:
The function `makeAPile` takes a positive integer `n` as input. It initializes an empty array `result` to store the number of stones in each level, and two variables `level` and `stones` to keep track of the current level and the number of stones in that level, respectively.

The function then enters a while loop that continues until there are no more stones left. In each iteration of the loop, it adds the current number of stones to the `result` array, updates the number of stones in the next level based on whether the current level is even or odd, and increments the level.

Finally, the function returns the `result` array, which contains the number of stones in each level of the pile. For example, if `n` is 3, the function will return `[3, 5, 7]`, which represents the number of stones in each level of the pile.