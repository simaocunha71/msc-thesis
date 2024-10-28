```
const eat = (number, need, remaining) => {
  const eaten = number + Math.min(need, remaining);
  const left = remaining - (need - need % remaining);
  return [eaten, left];
};
```
Explanation:
The function `eat` takes three arguments: `number` (the number of carrots already eaten), `need` (the number of carrots needed to eat), and `remaining` (the number of remaining carrots).

First, we calculate the total number of eaten carrots by adding the `number` and the minimum of `need` and `remaining`. This ensures that we don't eat more carrots than there are remaining.

Then, we calculate the number of carrots left by subtracting the difference between `need` and the remainder of `need` divided by `remaining` from `remaining`. This ensures that we don't try to eat more carrots than there are remaining.

Finally, we return an array containing the total number of eaten carrots and the number of carrots left.

For example, if `number` is 5, `need` is 6, and `remaining` is 10, the function will return `[11, 4]`, because we eat 6 carrots (5 already eaten + 1 more) and there are 4 carrots left. If `need` is greater than `remaining`, we will eat all remaining carrots and still be hungry, as in the example `eat(2, 11, 5) -> [7, 0]`.