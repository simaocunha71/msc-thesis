  let result = {};
  let maxCount = 0;
  let maxLetters = [];

  let words = test.split(' ');
  for (let word of words) {
    for (let letter of word) {
      if (result[letter]) {
        result[letter]++;
      } else {
        result[letter] = 1;
      }
    }
  }

  for (let key in result) {
    if (result[key] > maxCount) {
      maxCount = result[key];
      maxLetters = [key];
    } else if (result[key] == maxCount) {
      maxLetters.push(key);
    }
  }

  let finalResult = {};
  for (let letter of maxLetters) {
    finalResult[letter] = maxCount;
  }

  return finalResult;
}