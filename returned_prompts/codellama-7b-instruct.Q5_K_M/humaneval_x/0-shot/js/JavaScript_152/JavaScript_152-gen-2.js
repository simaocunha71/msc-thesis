
const compare = (game, guess) => {
  return game.map((g, i) => Math.abs(g - guess[i]));
};

