  return game.map((score, index) => Math.abs(score - guess[index]));
}
// This function uses the map() method to create a new array where each element is the result of a function
// applied to the corresponding element of the input array. The function used here is Math.abs(score - guess[index]),
// which calculates the absolute difference between the score and the guess for each match. This result is then returned
// as the new array.