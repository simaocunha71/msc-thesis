```javascript
const compare = (game, guess) => {
  return game.map((score, index) => Math.abs(score - guess[index]));
};
```
This solution uses the map() method to iterate over the game array and for each index, it calculates the absolute difference between the score and the corresponding guess. This difference is then returned as the value for that index in the new array. The map() method returns a new array with the results of the callback function applied to each element in the original array.