  let result = [];
  game.forEach((g, i) => {
    result.push(Math.abs(g - guess[i]));
  });

  return result;
}



