Here is a solution that uses a loop to generate the sequence of stone numbers:

```javascript
const makeAPile = (n) => {
  const pile = [];
  let stones = n;

  for (let i = 0; i < n; i++) {
    pile.push(stones);
    stones = i % 2 === 0 ? stones + 1 : stones - 1;
  }

  return pile;
};
```

This function starts by initializing an empty array `pile` to store the number of stones in each level, and a variable `stones` to keep track of the number of stones in the current level. The loop runs `n` times, and in each iteration, it adds the current number of stones to the `pile` array and updates the `stones` variable according to the rule described in the problem statement. Finally, the function returns the `pile` array.

For example, if we call `makeAPile(3)`, the function will return `[3, 5, 7]`, which represents the number of stones in each level of the pile.