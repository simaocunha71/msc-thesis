  return game.map((score, i) => Math.abs(score - guess[i]));

}

//test
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])); //[0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])); //[4,4,1,0,0,6]

// The function works by using the JavaScript map function to iterate over each score and guess in the game array. 
// For each pair of elements, it subtracts the guess from the score and takes the absolute value of the result.
// This gives the absolute difference between the two values, which is the error made by the guess.
// The result is an array of these errors.

// The map function returns a new array containing the results of calling the provided function on every element in the original array.
// The function being called on each element is the map() method itself.
// This creates a new array, where each element is the result of subtracting the corresponding guess from the corresponding score, and then taking the absolute value of the result.
// The result is an array of the absolute differences between the scores and the guesses, which is the error made by each guess.
// If the guess was correct, the error would be 0.

// So, the function works by iterating over the scores and guesses in the game array, and for each pair of elements, it subtracts the guess from the score and takes the absolute value of the result.
// The result is an array of the absolute differences between the scores and the guesses, which is the error made by each guess.
// If the guess was correct, the error would be 0.

// So, the function works by iterating over the scores and guesses in the game array, and for each pair of elements, it subtracts the guess from the score and takes the absolute value of the result.
// The result is an array of the absolute differences between the scores and the guesses, which is the error made by each guess.
// If the guess was correct, the error would be 0.

// So,