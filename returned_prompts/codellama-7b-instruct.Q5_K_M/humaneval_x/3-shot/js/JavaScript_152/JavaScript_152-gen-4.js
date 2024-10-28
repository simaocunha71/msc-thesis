  return game.map((e,i) => {
    if (e == guess[i]) return 0;
    else return Math.abs(e - guess[i]);
  });
}



