
}
*/

SOLUTION:

const compare = (game, guess) => {
  let result = [];
  for(let i = 0; i < game.length; i++) {
    result.push(Math.abs(game[i] - guess[i] ));
  }
  return result;
}

console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])); // [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])); // [4,4,1,0,0,6]

The function takes in two arrays, game and guess, and uses a for loop to iterate through each element in the arrays. It then pushes the absolute difference between each element in the arrays to the result array. Finally, it returns the result array.


A: You can use the map function with a lambda function (anonymous function) to iterate over the arrays and calculate the absolute difference for each pair of corresponding elements.

Here is a simple example:

```javascript
const compare = (game, guess) => 
  game.map((score, index) => Math.abs(score - guess[index]));
```

In this function, `map` is used to iterate over the `game` array. For each element in `game`, a function is executed that takes the element (`score`) and the index of the element in the `game` array (`index`). The function returns the absolute difference between the corresponding element in the `guess` array and the `score`.

This function returns a new array with the results.

For example:

```javascript
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])); // [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])); // [4,4,1,0,0,6]
```