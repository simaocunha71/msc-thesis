
const findMax = (words) => {
  let max = 0;
  let maxWord;
  const uniqueChars = new Set();
  for (let word of words) {
    uniqueChars.clear();
    for (let char of word) {
      if (!uniqueChars.has(char)) {
        uniqueChars.add(char);
      }
    }
    if (uniqueChars.size > max) {
      max = uniqueChars.size;
      maxWord = word;
    }
  }
  return maxWord;
};

