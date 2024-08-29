  const unique_chars_count = (word) => {
    const char_set = new Set();
    for (const c of word) {
      char_set.add(c);
    }
    return char_set.size;
  };

  let max_chars = 0;
  let max_word = '';

  for (const word of words) {
    const chars = unique_chars_count(word);
    if (chars > max_chars) {
      max_chars = chars;
      max_word = word;
    } else if (chars == max_chars && word < max_word) {
      max_word = word;
    }
  }

  return max_word;
}



