  var maxWord = "";
  var maxUniqueChars = 0;

  for (const word of words) {
    const uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars == maxUniqueChars) {
      maxWord = word < maxWord ? word : maxWord;
    }
  }

  return maxWord;
}



