  const max = Math.max(...words.map(word => word.length));
  const candidates = words.filter(word => word.length === max);

  const maxUniqueChars = candidates.map(word => {
    const uniqueChars = [...new Set(word)];
    return { word, uniqueChars };
  }).sort((a, b) => a.word.localeCompare(b.word));

  return maxUniqueChars[0].word;
}



