The task is to determine how far off each guess was in a series of matches. We can achieve this by subtracting the guess from the score for each match. If the guess is correct, the result will be 0; otherwise, it will be the absolute difference between the guess and the score.

Here is the solution in JavaScript:

```javascript
const compare = (game, guess) => {
    return game.map((score, index) => Math.abs(score - guess[index]));
};
```

In this code, the `map` method is used to iterate over the `game` array and perform the calculation for each match. The `Math.abs` function is used to get the absolute difference between the guess and the score, as the difference can be negative if the guess is higher than the score.

The function returns a new array with the same length as the `game` array, where each element represents how far off each guess was. If the guess is correct, the value is 0; otherwise, it is the absolute difference between the guess and the score.