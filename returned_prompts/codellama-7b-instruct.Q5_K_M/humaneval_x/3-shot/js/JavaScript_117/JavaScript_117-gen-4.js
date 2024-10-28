  var words = s.split(" ");
  var result = [];

  for (var word of words) {
    if (countConsonants(word) == n) {
      result.push(word);
    }
  }

  return result;
}



