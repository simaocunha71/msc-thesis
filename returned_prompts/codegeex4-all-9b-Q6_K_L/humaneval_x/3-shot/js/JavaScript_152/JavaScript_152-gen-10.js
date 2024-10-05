  var result = [];

  for (let i = 0; i < game.length; i++) {
    let difference = Math.abs(game[i] - guess[i]);
    result.push(difference);
  }

  return result;
}



