  let count = {};
  let words = test.split(' ');
  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    if (count[word]) {
      count[word]++;
    } else {
      count[word] = 1;
    }
  }
  let maxCount = 0;
  for (let word in count) {
    if (count[word] > maxCount) {
      maxCount = count[word];
    }
  }
  let result = {};
  for (let word in count) {
    if (count[word] === maxCount) {
      result[word] = count[word];
    }
  }
  return result;
}



