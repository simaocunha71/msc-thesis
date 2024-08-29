  const max = Math.max(...words.map(word => word.length));
  const maxWords = words.filter(word => word.length == max);

  const maxChar = maxWords.map(word => {
    const uniqueChars = new Set(word);
    return {word, uniqueChars};
  });

  maxChar.sort((a, b) => {
    return a.word.localeCompare(b.word);
  });

  return maxChar[0].word;
}



