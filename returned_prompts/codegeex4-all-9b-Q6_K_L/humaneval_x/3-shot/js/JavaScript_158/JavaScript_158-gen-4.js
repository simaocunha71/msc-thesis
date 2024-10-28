  var max_word = '';
  var max_unique_chars = 0;

  for (const word of words) {
    let unique_chars = new Set(word);
    if (unique_chars.size > max_unique_chars) {
      max_unique_chars = unique_chars.size;
      max_word = word;
    } else if (unique_chars.size == max_unique_chars) {
      if (word < max_word) {
        max_word = word;
      }
    }
  }

  return max_word;
}