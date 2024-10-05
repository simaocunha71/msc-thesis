  let max_word = '';
  let max_chars = 0;

  for (const word of words) {
    const unique_chars = new Set(word).size;
    if (unique_chars > max_chars) {
      max_chars = unique_chars;
      max_word = word;
    } else if (unique_chars == max_chars) {
      if (word < max_word) {
        max_word = word;
      }
    }
  }
  return max_word;
}