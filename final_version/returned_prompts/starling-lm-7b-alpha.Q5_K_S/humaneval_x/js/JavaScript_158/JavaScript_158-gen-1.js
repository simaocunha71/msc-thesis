  let max = 0;
  let maxWord = '';

  for (const word of words) {
    const unique_chars = new Set(word.split(''));
    const unique_length = unique_chars.size;

    if (max < unique_length) {
      max = unique_length;
      maxWord = word;
    } else if (max === unique_length) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  }

  return maxWord;
}



