  var max_word = "";
  var max_length = 0;
  var unique_chars = [];
  var current_length = 0;

  for (const word of words) {
    for (const char of word) {
      if (unique_chars.includes(char)) {
        continue;
      } else {
        unique_chars.push(char);
        current_length += 1;
      }
    }

    if (current_length > max_length) {
      max_word = word;
      max_length = current_length;
    }
    current_length = 0;
    unique_chars = [];
  }

  return max_word;
}



