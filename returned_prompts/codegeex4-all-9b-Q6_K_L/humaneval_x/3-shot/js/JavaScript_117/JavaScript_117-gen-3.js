  var words = s.split(' ');
  var result = [];
  for (var i = 0; i < words.length; i++) {
    var word = words[i];
    var consonants = 0;
    for (var j = 0; j < word.length; j++) {
      var c = word[j];
      if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
        consonants += 1;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }
  return result;
}