  return game.map((score, index) => {
    if (score === guess[index]) {
      return 0;
    } else {
      return Math.abs(score - guess[index]);
    }
  });
}



