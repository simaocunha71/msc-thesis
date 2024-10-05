const compare = (game, guess) => {
  let gameScore = game.map((item, index) => item - guess[index]);
  return gameScore;
}

B:
const compare = (game, guess) => {
  let gameScore = game.map((item, index) => Math.abs(item - guess[index]));
  return gameScore;
}

C:
const compare = (game, guess) => {
  let gameScore = game.map((item, index) => item == guess[index] ? 0 : Math.abs(item - guess[index]));
  return gameScore;
}

D:
const compare = (game, guess) => {
  let gameScore = game.map((item, index) => item == guess[index] ? 0 : Math.abs(item - guess[index])).filter(item => item != 0);
  return gameScore;
}

E:
const compare = (game, guess) => {
  let gameScore = game.map((item, index) => item == guess[index] ? 0 : Math.abs(item - guess[index])).reduce((a, b) => a + b, 0);
  return gameScore;
}

F:
const compare = (game, guess) => {
  let gameScore = game.map((item, index) => item == guess[index] ? 0 : Math.abs(item - guess[index])).map(item => item * item);
  return gameScore;
}
