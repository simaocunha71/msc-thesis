  const getUniqueCharCount = (word) => {
    const wordSet = new Set(word.split(''));
    return wordSet.size;
  };

  let maxCount = 0;
  let maxWord = '';

  for (const word of words) {
    const count = getUniqueCharCount(word);
    if (count > maxCount) {
      maxWord = word;
      maxCount = count;
    } else if (count == maxCount) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  }

  return maxWord;
}



