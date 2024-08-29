  const result = [];
  for (let i = 0; i < game.length; i++) {
    result[i] = Math.abs(game[i] - guess[i]);
  }
  return result;
}



