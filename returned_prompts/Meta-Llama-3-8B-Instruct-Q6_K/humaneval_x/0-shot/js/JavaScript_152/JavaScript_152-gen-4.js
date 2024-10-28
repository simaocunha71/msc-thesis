Here is a solution that uses the map function to iterate over the two arrays and calculate the absolute difference between the score and the guess for each match. If the guess is equal to the score, the function returns an array with zeros.

```javascript
const compare = (game, guess) => game.map((score, index) => Math.abs(score - guess[index]));
```

You can test this function with the examples you provided:

```javascript
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])); // [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])); // [4,4,1,0,0,6]
```


This solution assumes that the input arrays are of equal length and that the indices of the arrays correspond to the same matches. It also assumes that the scores and guesses are valid (i.e., they are numbers). If the input arrays are not of equal length or if the indices do not correspond to the same matches, the function will return incorrect results. If the scores or guesses are not valid, the function will throw an error.