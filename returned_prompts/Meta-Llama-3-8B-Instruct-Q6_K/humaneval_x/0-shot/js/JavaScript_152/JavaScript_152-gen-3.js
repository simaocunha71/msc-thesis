The problem is asking to compare the scores with the guesses and return an array of the same length with the absolute difference between the score and the guess. If the guess is correct, the absolute difference is 0.

Here is the solution:
```
const compare = (game, guess) => game.map((score, index) => Math.abs(score - guess[index]));
```
This function uses the `map` method to iterate over the `game` array and for each score, it calculates the absolute difference with the corresponding guess from the `guess` array using `Math.abs`. The result is an array of the same length as the input arrays, where each element represents the absolute difference between the score and the guess.

Let's test the function with the examples you provided:
```
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])); // [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])); // [4,4,1,0,0,6]
```
Both outputs match the expected results.