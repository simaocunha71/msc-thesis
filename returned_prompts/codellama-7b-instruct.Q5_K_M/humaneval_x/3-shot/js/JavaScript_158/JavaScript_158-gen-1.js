  var max_length = 0;
  var max_word = "";

  for (var word of words) {
    if (max_length < word.length) {
      max_length = word.length;
      max_word = word;
    }
  }

  return max_word;
}



