Here is the solution using JavaScript:

```javascript
const compare = (game, guess) => {
  return game.map((score, index) => Math.abs(score - guess[index]));
};
```
The function `compare` takes two arrays `game` and `guess` as arguments. It returns a new array where each element is the absolute difference between the corresponding elements in `game` and `guess`. The `map` method is used to iterate over the elements of `game` and for each element, it calculates the absolute difference with the corresponding element in `guess` and returns a new array with these differences. The `Math.abs` method is used to get the absolute value of the difference.

For example, if we call `compare([1,2,3,4,5,1],[1,2,3,4,2,-2])`, the function will return `[0,0,0,0,3,3]`. And if we call `compare([0,5,0,0,0,4],[4,1,1,0,0,-2])`, the function will return `[4,4,1,0,0,6]`.