  let maxUniqueChars = 0;
  let wordWithMaxUniqueChars = '';

  words.forEach(word => {
    const uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      wordWithMaxUniqueChars = word;
    } else if (uniqueChars === maxUniqueChars) {
      wordWithMaxUniqueChars = word < wordWithMaxUniqueChars ? word : wordWithMaxUniqueChars;
    }
  });

  return wordWithMaxUniqueChars;
}



