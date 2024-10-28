  return game.map((score, idx) => {
    if (score == guess[idx]) {
      return 0;
    } else {
      return Math.abs(score - guess[idx]);
    }
  });
}



