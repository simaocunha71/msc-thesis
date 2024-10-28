const findMax = (words) => {
  var uniqueChars = new Set();
  var maxLength = 0;
  var maxWord = "";
  for (var i = 0; i < words.length; i++) {
    if (words[i].length > maxLength) {
      maxLength = words[i].length;
      maxWord = words[i];
    }
    if (words[i].length === maxLength) {
      for (var j = 0; j < words[i].length; j++) {
        if (uniqueChars.has(words[i][j])) {
          maxLength = words[i].length;
          maxWord = words[i];
        } else {
          uniqueChars.add(words[i][j]);
        }
      }
    }
  }
  return maxWord;
};

