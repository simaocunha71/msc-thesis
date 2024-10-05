  var max = 0;
  var max_word = "";
  for (var word of words) {
    var unique_chars = new Set(word);
    if (unique_chars.size > max) {
      max = unique_chars.size;
      max_word = word;
    } else if (unique_chars.size == max && word < max_word) {
      max_word = word;
    }
  }
  return max_word;
}



