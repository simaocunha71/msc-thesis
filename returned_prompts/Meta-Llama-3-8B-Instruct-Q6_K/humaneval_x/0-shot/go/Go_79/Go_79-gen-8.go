The task is to determine how far off each guess was from the actual score in a series of matches. If the guess is correct, the value is 0, and if not, the value is the absolute difference between the guess and the score.

Here is a simple JavaScript function that accomplishes this:

```javascript
const compare = (game, guess) => {
    return game.map((score, index) => Math.abs(score - guess[index]));
};
```

This function uses the `map` method to iterate over the `game` array, and for each element, it calculates the absolute difference between the score and the guess at the same index. The result is an array of the same length as the input arrays, where each element represents how far off the guess was from the actual score.

For example, if you call `compare([1,2,3,4,5,1],[1,2,3,4,2,-2])`, the function will return `[0,0,0,0,3,3]`, indicating that the first three guesses were correct and the last two were off by 3 and 3, respectively. If you call `compare([0,5,0,0,0,4],[4,1,1,0,0,-2])`, the function will return `[4,4,1,0,0,6]`, indicating that the first two guesses were off by 4, the third was off by 1, and the last two were correct.