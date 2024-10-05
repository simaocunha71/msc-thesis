  var max_word = "";
  var max_count = 0;

  for (const word of words) {
    var count = new Set(word).size;
    if (count > max_count) {
      max_count = count;
      max_word = word;
    } else if (count == max_count) {
      max_word = word < max_word ? word : max_word;
    }
  }

  return max_word;
}