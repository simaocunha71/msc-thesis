Here is a simple JavaScript function that implements the problem:

```javascript
const makeAPile = (n) => {
  const pile = [];
  let stones = n;

  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      pile.push(stones);
      stones += 2;
    } else {
      pile.push(stones);
      stones += 1;
    }
  }

  return pile;
};
```
This function initializes an empty array `pile` and a variable `stones` set to the input `n`. It then enters a loop that runs `n` times. Inside the loop, it checks whether the current iteration `i` is even or odd using the modulo operator (`%`). If `i` is even, it adds `stones` to the `pile` array and increments `stones` by 2. If `i` is odd, it adds `stones` to the `pile` array and increments `stones` by 1. Finally, it returns the `pile` array. 

You can test this function with the example input `3` to get the output `[3, 5, 7]`. 

This function assumes that the input `n` is a positive integer. If the input can be negative or non-integer, you may need to add error handling or validation. 