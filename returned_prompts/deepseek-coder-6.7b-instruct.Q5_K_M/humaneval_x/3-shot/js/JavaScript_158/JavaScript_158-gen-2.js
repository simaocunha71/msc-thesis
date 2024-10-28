  let maxUniqueChars = 0;
  let wordWithMaxUniqueChars = '';

  for (let word of words) {
    const uniqueChars = new Set(word.split(''));
    if (uniqueChars.size > maxUniqueChars) {
      maxUniqueChars = uniqueChars.size;
      wordWithMaxUniqueChars = word;
    } else if (uniqueChars.size === maxUniqueChars) {
      wordWithMaxUniqueChars = word < wordWithMaxUniqueChars ? word : wordWithMaxUniqueChars;
    }
  }

  return wordWithMaxUniqueChars;
}



