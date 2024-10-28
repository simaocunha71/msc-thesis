  let letterCount = {};

  if (test.length > 0) {
    let words = test.split(' ');
    for (let word of words) {
      for (let letter of word) {
        if (letterCount[letter]) {
          letterCount[letter]++;
        } else {
          letterCount[letter] = 1;
        }
      }
    }
  }

  let maxCount = Math.max(...Object.values(letterCount));
  let maxLetters = Object.keys(letterCount).filter(letter => letterCount[letter] === maxCount);

  let result = {};
  for (let letter of maxLetters) {
    result[letter] = maxCount;
  }

  return result;
}