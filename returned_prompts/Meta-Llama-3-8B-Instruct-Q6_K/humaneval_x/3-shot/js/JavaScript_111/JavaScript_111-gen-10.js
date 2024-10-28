  let result = {};
  let maxCount = 0;
  let maxCountLetters = [];

  if (test === '') {
    return {};
  }

  let words = test.split(' ');
  for (let word of words) {
    let letter = word[0];
    let count = 0;
    for (let c of word) {
      if (c === letter) {
        count++;
      }
    }
    if (count > maxCount) {
      maxCount = count;
      maxCountLetters = [letter];
    } else if (count === maxCount) {
      maxCountLetters.push(letter);
    }
  }
  result = {};
  for (let letter of maxCountLetters) {
    result[letter] = maxCount;
  }
  return result;
} 



