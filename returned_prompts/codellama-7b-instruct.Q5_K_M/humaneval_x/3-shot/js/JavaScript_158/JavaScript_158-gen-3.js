  var max_word = "";
  var max_count = 0;

  for (var i = 0; i < words.length; i++) {
    var word = words[i];
    var count = new Set(word).size;
    if (count > max_count || (count == max_count && word < max_word)) {
      max_count = count;
      max_word = word;
    }
  }

  return max_word;
}



