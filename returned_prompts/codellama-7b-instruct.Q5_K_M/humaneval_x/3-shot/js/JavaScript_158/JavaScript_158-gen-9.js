  var max_word = words[0];
  var max_unique_chars = getUniqueChars(max_word).length;

  for (var word of words) {
    var unique_chars = getUniqueChars(word);
    var unique_chars_len = unique_chars.length;
    if (unique_chars_len > max_unique_chars) {
      max_word = word;
      max_unique_chars = unique_chars_len;
    } else if (unique_chars_len == max_unique_chars) {
      if (word < max_word) {
        max_word = word;
      }
    }
  }
  return max_word;

  function getUniqueChars(word) {
    var unique_chars = [];
    for (const char of word) {
      if (unique_chars.indexOf(char) === -1) {
        unique_chars.push(char);
      }
    }
    return unique_chars;
  }
}



