  return game.map((score, index) => {
    if (guess[index] === score) {
      return 0;
    } else {
      return Math.abs(guess[index] - score);
    }
  });
}