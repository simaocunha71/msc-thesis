  let maxWord = '';
  let maxCount = 0;

  for (const word of words) {
    const uniqueChars = new Set(word).size;
    if (uniqueChars > maxCount) {
      maxCount = uniqueChars;
      maxWord = word;
    }
  }

  return maxWord;
}