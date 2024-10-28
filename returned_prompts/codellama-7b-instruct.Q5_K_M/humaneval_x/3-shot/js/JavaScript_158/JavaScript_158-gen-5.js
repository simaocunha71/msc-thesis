  var max = 0, index = 0;
  for (var i = 0; i < words.length; i++) {
    var current = [...new Set(words[i])].length;
    if (current > max) {
      max = current;
      index = i;
    }
  }
  return words[index];
}



