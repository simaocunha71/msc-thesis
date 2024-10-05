Here is the solution using a simple loop:
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
This function initializes an empty list `pile` and a variable `level` to the input `n`. Then it loops `n` times. In each iteration, it adds the current `level` to the `pile` and updates `level` to the next odd or even number depending on whether `level` is even or odd. Finally, it returns the `pile`.