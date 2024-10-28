  let maxCount = 0;
  let maxWord = '';

  for (let word of words) {
    let uniqueChars = new Set(word.split(''));
    if (uniqueChars.size > maxCount) {
      maxCount = uniqueChars.size;
      maxWord = word;
    } else if (uniqueChars.size === maxCount) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
}



