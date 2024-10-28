Here is a simple JavaScript function that accomplishes the task:

```javascript
const compare = (game, guess) => {
    return game.map((score, index) => Math.abs(score - guess[index]));
}
```

This function uses the `map` method to iterate over the `game` array and calculate the absolute difference between each score and the corresponding guess. The result is an array of the same length as the input arrays, where each element represents how far off each guess was. If the guess is correct (i.e., the score is equal to the guess), the value is 0; otherwise, it is the absolute difference between the score and the guess.

Here is an explanation of how the function works:

1. `game.map((score, index) => ...)` iterates over the `game` array and applies the callback function to each element. The callback function takes two arguments: `score` and `index`.
2. `Math.abs(score - guess[index])` calculates the absolute difference between the current score and the corresponding guess.
3. The result is an array of the same length as the input arrays, where each element represents how far off each guess was.

Here are some test cases to demonstrate the function's behavior:

```javascript
console.log(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])); // [0, 0, 0, 0, 3, 3]
console.log(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2])); // [4, 4, 1, 0, 0, 6]
```