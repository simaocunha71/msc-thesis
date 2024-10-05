  let max_word = "";
  let max_char_count = 0;

  for (let word of words) {
    let char_count = new Set(word).size;
    if (char_count > max_char_count) {
      max_char_count = char_count;
      max_word = word;
    }
  }

  return max_word;
}



