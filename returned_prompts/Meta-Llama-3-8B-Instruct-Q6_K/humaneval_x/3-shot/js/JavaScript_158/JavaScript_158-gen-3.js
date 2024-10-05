  let max_word = '';
  let max_unique_chars = 0;

  for (const word of words) {
    let unique_chars = new Set(word).size;
    if (unique_chars > max_unique_chars) {
      max_word = word;
      max_unique_chars = unique_chars;
    } else if (unique_chars === max_unique_chars) {
      if (word < max_word) {
        max_word = word;
      }
    }
  }

  return max_word;
}