
const compare = (game, guess) => {
  const result = [];
  for (let i = 0; i < game.length; i++) {
    const diff = game[i] - guess[i];
    if (diff === 0) {
      result.push(0);
    } else {
      result.push(Math.abs(diff));
    }
  }
  return result;
};


B:

const compare = (game, guess) => {
  const result = [];
  for (let i = 0; i < game.length; i++) {
    result.push(Math.abs(game[i] - guess[i]));
  }
  return result;
};


C:

const compare = (game, guess) => {
  const result = [];
  for (let i = 0; i < game.length; i++) {
    result.push(Math.abs(game[i] - guess[i]) || 0);
  }
  return result;
};


D:

const compare = (game, guess) => {
  const result = [];
  for (let i = 0; i < game.length; i++) {
    if (game[i] === guess[i]) {
      result.push(0);
    } else {
      result.push(Math.abs(game[i] - guess[i]));
    }
  }
  return result;
};


E:

const compare = (game, guess) => {
  const result = [];
  for (let i = 0; i < game.length; i++) {
    if (game[i] === guess[i]) {
      result.push(0);
    } else {
      result.push(Math.abs(game[i] - guess[i]) || 0);
    }
  }
  return result;
};


F:

const compare = (game, guess) => {
  const result = [];
  for (let i = 0; i < game.length; i++) {
    if (game[i] === guess[i]) {
      result.