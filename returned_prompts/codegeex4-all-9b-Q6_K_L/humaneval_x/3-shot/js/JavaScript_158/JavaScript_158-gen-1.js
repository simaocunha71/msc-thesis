  let maxWord = "";
  let maxUniqueChars = 0;

  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    let uniqueChars = new Set();
    for (let j = 0; j < word.length; j++) {
      uniqueChars.add(word[j]);
    }
    if (uniqueChars.size > maxUniqueChars) {
      maxUniqueChars = uniqueChars.size;
      maxWord = word;
    }
  }

  return maxWord;
}