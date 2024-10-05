  let result = {};
  let maxCount = 0;
  let maxLetters = [];

  if (test === "") {
    return {};
  }

  let words = test.split(' ');
  for (let word of words) {
    for (let letter of word) {
      if (result[letter] === undefined) {
        result[letter] = 1;
      } else {
        result[letter]++;
      }
      if (result[letter] > maxCount) {
        maxCount = result[letter];
        maxLetters = [letter];
      } else if (result[letter] === maxCount) {
        maxLetters.push(letter);
      }
    }
  }
  return maxLetters.reduce((acc, current) => {
    acc[current] = maxCount;
    return acc;
  }, {});
} 



