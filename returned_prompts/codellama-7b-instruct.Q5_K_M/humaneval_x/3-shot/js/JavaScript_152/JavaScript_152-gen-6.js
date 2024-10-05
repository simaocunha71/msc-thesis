  let result = [];
  for (let i = 0; i < game.length; i++) {
    if (game[i] == guess[i]) {
      result.push(0);
    } else {
      result.push(Math.abs(game[i] - guess[i]));
    }
  }
  return result;
}



