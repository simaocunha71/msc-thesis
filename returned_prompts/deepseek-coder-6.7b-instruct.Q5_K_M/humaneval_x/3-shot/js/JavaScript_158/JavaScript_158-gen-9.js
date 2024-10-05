  let maxUniqueChars = 0;
  let maxWord = "";

  for (let word of words)  {
    let uniqueChars = new Set(word.split(''));
    if (uniqueChars.size > maxUniqueChars)  {
      maxUniqueChars = uniqueChars.size;
      maxWord = word;
    } else if (uniqueChars.size === maxUniqueChars)  {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
}



