The problem is asking to compare the scores and guesses of a game and return an array with the difference between the guess and the score for each match. If the guess is correct, the difference is 0, otherwise it's the absolute difference.

Here is the solution in JavaScript:

```javascript
const compare = (game, guess) => {
  return game.map((score, index) => Math.abs(score - guess[index]));
}
```

In this solution, we use the `map` method to create a new array with the same length as the input arrays. For each element in the array, we calculate the absolute difference between the score and the guess using `Math.abs(score - guess[index])`. The resulting array is then returned. 

Let's test the function with the examples provided:

```javascript
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])); // [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])); // [4,4,1,0,0,6]
```

The output matches the expected result. The function works correctly. 