  let maxWord = '';
  let maxUniqueChars = 0;

  for (const word of words) {
    let uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  }

  return maxWord;
}