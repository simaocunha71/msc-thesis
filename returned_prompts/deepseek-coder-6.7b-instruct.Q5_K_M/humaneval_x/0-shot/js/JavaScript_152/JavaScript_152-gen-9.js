  return game.map((score, i) => Math.abs(score - guess[i]));

};
*/

//Solution:
/*
The map function is used to iterate over the game array and for each match, it calculates the absolute difference between the score and the guess at the corresponding index of the guess array.
*/

//Test Cases:
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) // Expected: [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) // Expected: [4,4,1,0,0,6]

/*
The function works by taking two arrays as input, game and guess, both of equal length. It uses the map function to iterate over the game array and for each match, it calculates the absolute difference between the score and the guess at the corresponding index of the guess array. The function then returns an array of these differences.
*/

/*
In the test cases, the function correctly calculates the difference between the score and the guess for each match.
*/

//End Solution

/*
The overall time complexity of the solution is O(n), where n is the length of the input arrays. This is because the map function iterates over the game array once, and for each match, it performs a constant amount of work (calculating the absolute difference). Therefore, the total work done is proportional to the length of the input arrays, and the time complexity is linear.

The space complexity of the solution is also O(n), because the map function creates a new array of the same length as the input arrays. Therefore, the space complexity is linear in the size of the input.
*/

//End Q

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution

//End Solution