  var maxUnique = 0;
  var maxWord = "";

  for (let i = 0; i < words.length; i++) {
    var word = words[i];
    var uniqueChars = new Set(word);
    var uniqueCount = uniqueChars.size;
    if (uniqueCount > maxUnique) {
      maxUnique = uniqueCount;
      maxWord = word;
    }
  }

  return maxWord;
}



