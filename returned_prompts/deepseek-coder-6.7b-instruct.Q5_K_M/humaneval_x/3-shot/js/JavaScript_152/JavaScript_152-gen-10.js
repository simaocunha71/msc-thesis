  let result = [];
  for(let i=0; i<game.length; i++){
    result.push(Math.abs(game[i]-guess[i]));
  }
  return result;
}



