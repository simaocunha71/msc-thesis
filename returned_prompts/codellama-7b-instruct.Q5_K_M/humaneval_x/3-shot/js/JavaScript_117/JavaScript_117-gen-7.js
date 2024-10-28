  var result = [];
  var words = s.split(" ");
  for (const word of words) {
    var consonants = 0;
    for (const char of word) {
      if (char != "a" && char != "e" && char != "i" && char != "o" && char != "u") {
        consonants += 1;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }
  return result;
}



