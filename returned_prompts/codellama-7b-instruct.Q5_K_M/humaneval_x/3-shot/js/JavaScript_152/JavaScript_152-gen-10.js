  return game.map((score, idx) => {
    return Math.abs(score - guess[idx]);
  });
}



