  let max_length = 0;
  let max_word = '';
  let unique_chars = new Set();

  for (const word of words) {
    unique_chars = new Set();
    for (const char of word) {
      if (!unique_chars.has(char)) {
        unique_chars.add(char);
      }
    }
    if (max_length < unique_chars.size) {
      max_length = unique_chars.size;
      max_word = word;
    } else if (max_length === unique_chars.size && max_word > word) {
      max_word = word;
    }
  }
  return max_word;
}



