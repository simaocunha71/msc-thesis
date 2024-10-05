  let result = [];
  for(let i = 0; i < game.length; i++){
    result.push(Math.abs(game[i] - guess[i] ));
  }
  return result;
}
*/

const compare = (game, guess) => game.map((score, i) => Math.abs(score - guess[i]));

//Test cases
console.log(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])); // [0, 0, 0, 0, 3, 3]
console.log(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2])); // [4, 4, 1, 0, 0, 6]
```

## Solution Explanation

The task is to compare the scores of the matches of two arrays. The score of the match is the absolute difference between the actual score and the guessed score.

In JavaScript, you can use the `map()` method on the `game` array to iterate over each score and its index. For each score, you calculate the absolute difference between the score and the guessed score at the same index in the `guess` array. The `Math.abs()` function is used to ensure the result is positive, regardless of the sign of the difference.

Finally, the function returns the resulting array.

## Code Explanation

- The `compare` function takes two parameters: `game` and `guess`.
- The `map()` method is called on the `game` array. This method creates a new array with the results of calling a provided function on every element in the calling array.
- Inside the `map()` callback, `score` is the current element being processed and `i` is the index of the current element.
- The function returns the absolute difference between `score` and the element at the same index in the `guess` array (`guess[i]`).
- This new array is returned as the result.

## Test Cases

The test cases use