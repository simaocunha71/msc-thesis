This problem can be solved by comparing the elements of the two arrays and calculating the absolute difference between the corresponding elements. If the elements are equal, the difference is 0. If the elements are not equal, the difference is the absolute value of the difference.

Here is the solution in JavaScript:
```
const compare = (game, guess) => {
  return game.map((score, index) => Math.abs(score - guess[index]));
};
```
This function uses the `map` method to iterate over the `game` array and calculate the absolute difference between each element of the `game` array and the corresponding element of the `guess` array. The result is an array of the same length as the input arrays, where each element represents the difference between the corresponding elements of the input arrays.

For example, if the input arrays are `[1, 2, 3, 4, 5, 1]` and `[1, 2, 3, 4, 2, -2]`, the output will be `[0, 0, 0, 0, 3, 3]`.

You can test this function with different input arrays to see that it produces the correct output. For example:
```
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])); // [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])); // [4,4,1,0,0,6]
``` 