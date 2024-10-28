  let maxUniqueChars = 0;
  let maxWord = '';

  words.forEach((word) => {
    const uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      maxWord = maxWord < word ? maxWord : word;
    }
  });

  return maxWord;
}



