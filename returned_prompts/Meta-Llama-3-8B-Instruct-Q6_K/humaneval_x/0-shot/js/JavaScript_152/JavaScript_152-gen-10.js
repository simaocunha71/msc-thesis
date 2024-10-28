Here is the JavaScript code to solve the problem:

```javascript
const compare = (game, guess) => {
  return game.map((score, index) => Math.abs(score - guess[index]));
};
```

This function takes two arrays, `game` and `guess`, as input. It then uses the `map` method to iterate over the elements of `game` and calculates the absolute difference between each score and the corresponding guess. The result is an array of the same length as `game`, where each element represents how far off the guess was for that match. If the guess was correct, the value is 0. Otherwise, the value is the absolute difference between the guess and the score.