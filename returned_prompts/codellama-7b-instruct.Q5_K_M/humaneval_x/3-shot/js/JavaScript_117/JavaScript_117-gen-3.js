  var result = [];
  var words = s.split(' ');
  for (var word of words) {
    var vowels = ['a', 'e', 'i', 'o', 'u'];
    var consonants = [];
    for (var i = 0; i < word.length; i++) {
      if (vowels.indexOf(word[i]) == -1) {
        consonants.push(word[i]);
      }
    }
    if (consonants.length == n) {
      result.push(word);
    }
  }

  return result;
}



