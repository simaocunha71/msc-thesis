const histogram = (test) => {
  const letters = test.split(" ").reduce((acc, letter) => {
    if (letter in acc) {
      acc[letter]++;
    } else {
      acc[letter] = 1;
    }
    return acc;
  }, {});

  const max = Math.max(...Object.values(letters));

  return Object.keys(letters)
    .filter((letter) => letters[letter] === max)
    .reduce((acc, letter) => {
      acc[letter] = max;
      return acc;
    }, {});
};
*/