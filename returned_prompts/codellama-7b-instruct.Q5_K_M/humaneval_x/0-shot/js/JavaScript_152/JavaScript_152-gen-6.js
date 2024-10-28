
/*
I will use the .map() method to iterate over the guesses array.
For each iteration, I will find the corresponding index of the score array based on the current index of the guesses array.
I will then compare the current guess to the corresponding score.
If the guess is correct, I will return 0.
If the guess is not correct, I will return the absolute difference between the guess and the score.

Finally, I will use the .map() method again to iterate over the array of differences and return a new array with the same length as the guesses array.
*/

const compare = (game, guess) => {
  return guess.map((guess, i) => {
    if (guess === game[i]) {
      return 0
    } else {
      return Math.abs(guess - game[i])
    }
  })
}

// B:
/*
I will use the .map() method to iterate over the guesses array.
For each iteration, I will find the corresponding index of the score array based on the current index of the guesses array.
I will then compare the current guess to the corresponding score.
If the guess is correct, I will return a new array with the current index set to 0.
If the guess is not correct, I will return a new array with the current index set to the absolute difference between the guess and the score.

Finally, I will use the .map() method again to iterate over the array of differences and return a new array with the same length as the guesses array.
*/

const compare = (game, guess) => {
  return guess.map((guess, i) => {
    if (guess === game[i]) {
      return [0]
    } else {
      return [Math.abs(