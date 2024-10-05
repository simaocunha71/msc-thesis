  if (!test) {
    return {};
  }
  let letterCount = {};
  let maxCount = 0;

  for (const letter of test.split(' ')) {
    if (letterCount[letter]) {
      letterCount[letter]++;
    } else {
      letterCount[letter] = 1;
    }
    if (letterCount[letter] > maxCount) {
      maxCount = letterCount[letter];
    }
  }

  let maxLetters = Object.keys(letterCount).filter((key) => letterCount[key] === maxCount);
  let result = {};
  for (const letter of maxLetters) {
    result[letter] = maxCount;
  }
  return result;
}