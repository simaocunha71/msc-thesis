  var maxUnique = 0;
  var maxWord = "";
  for (var word of words) {
    var uniqueChars = new Set(word).size;
    if (uniqueChars > maxUnique) {
      maxUnique = uniqueChars;
      maxWord = word;
    } else if (uniqueChars == maxUnique) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  }
  return maxWord;
}