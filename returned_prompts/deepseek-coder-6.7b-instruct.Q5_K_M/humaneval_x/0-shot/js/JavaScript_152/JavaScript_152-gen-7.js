  return game.map((score, i) => Math.abs(score - guess[i]));

}

console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) //-> [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) //-> [4,4,1,0,0,6]

// In the map function, we are mapping through each item in the 'game' array.
// For each item, we are returning the absolute difference between the item at the same index in the 'guess' array and the item from the 'game' array.
// This is done by using the built-in Math.abs function to get the absolute value of the difference.
// The resulting array is then returned.

// This solution assumes that the 'game' and 'guess' arrays are of equal length. If this is not the case, you may want to add some error checking to handle this situation.

*/

// Solution
const compare = (game, guess) => {
  let results = [];
  for (let i = 0; i < game.length; i++) {
    results.push(Math.abs(game[i] - guess[i]));
  }
  return results;
};

console.log(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])); //-> [0, 0, 0, 0, 3, 3]
console.log(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2])); //-> [4, 4, 1, 0, 0, 6]

// In this solution, we are using a for loop to iterate through each item in the 'game' array.
// For each item, we are calculating the absolute difference between the item at the same index in the 'guess' array and the item