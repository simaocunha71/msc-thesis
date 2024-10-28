  return game.map((score, i) => Math.abs(score - guess[i]));
}
// This function uses the map() method to create a new array with the results of the callback function applied to each element of the game array. 
// The callback function takes two arguments, score and i, where score is the element of the game array and i is its index. 
// It calculates the absolute difference between the score and the corresponding element of the guess array and returns this value. 
// The resulting array contains the distance of each guess from the score, which is what the problem requires.