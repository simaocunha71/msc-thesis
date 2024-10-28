  let maxUniqueChars = 0;
  let maxWord = '';

  for (let word of words) {
    let uniqueCharsCount = new Set(word).size;
    if (uniqueCharsCount > maxUniqueChars) {
      maxUniqueChars = uniqueCharsCount;
      maxWord = word;
    } else if (uniqueCharsCount === maxUniqueChars) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
}


