The problem is asking you to compare the scores and guesses for each match in a game, and return an array with the absolute difference between the score and the guess for each match. If the guess is correct (i.e., the score is equal to the guess), the absolute difference is 0.

Here's a JavaScript function that accomplishes this:

```javascript
const compare = (game, guess) => {
  return game.map((score, index) => Math.abs(score - guess[index]));
}
```

This function uses the `map` method to iterate over the `game` array and calculate the absolute difference between each score and the corresponding guess. The result is an array of the same length as the input arrays, where each element is the absolute difference between the score and the guess for the corresponding match.

For example, if you call `compare([1,2,3,4,5,1],[1,2,3,4,2,-2])`, the function will return `[0,0,0,0,3,3]`, which are the absolute differences between the scores and guesses for each match. If you call `compare([0,5,0,0,0,4],[4,1,1,0,0,-2])`, the function will return `[4,4,1,0,0,6]`, which are the absolute differences between the scores and guesses for each match.