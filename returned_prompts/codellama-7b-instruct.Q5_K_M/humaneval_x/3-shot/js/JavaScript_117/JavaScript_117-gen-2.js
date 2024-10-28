  var result = [];
  var words = s.split(' ');
  for (var i = 0; i < words.length; i++) {
    if (countConsonants(words[i]) == n) {
      result.push(words[i]);
    }
  }
  return result;
}



