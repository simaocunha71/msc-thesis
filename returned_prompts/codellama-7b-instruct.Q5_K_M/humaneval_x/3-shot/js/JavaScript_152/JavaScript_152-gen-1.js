  var result = [];
  for (let i = 0; i < game.length; i++) {
    if (game[i] == guess[i]) {
      result.push(0);
    } else {
      result.push(Math.abs(guess[i] - game[i]));
    }
  }
  return result;
}



