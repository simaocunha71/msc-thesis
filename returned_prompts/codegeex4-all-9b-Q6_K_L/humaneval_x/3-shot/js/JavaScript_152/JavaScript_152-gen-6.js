  let results = []
  for(let i = 0; i < game.length; i++){
    results.push(Math.abs(game[i] - guess[i]))
  }
  return results
}



