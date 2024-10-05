  return game.map((score, index) => (guess[index] === score) ? 0 : Math.abs(guess[index] - score));
}



