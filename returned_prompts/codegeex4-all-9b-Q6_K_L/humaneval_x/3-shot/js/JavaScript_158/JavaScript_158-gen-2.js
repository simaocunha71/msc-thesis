  var max = 0;
  var result = "";

  for (const word of words) {
    var unique = new Set(word);
    if (unique.size > max) {
      max = unique.size;
      result = word;
    } else if (unique.size == max) {
      if (word < result) {
        result = word;
      }
    }
  }

  return result;
}



