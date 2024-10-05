  var consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
  var vowels = "aeiouAEIOU";

  var i = word.length - 1;
  while (i >= 0) {
    if (vowels.indexOf(word[i]) != -1) {
      if (i == 0) {
        return "";
      } else {
        if (consonants.indexOf(word[i - 1]) != -1) {
          return word[i];
        }
      }
    } else if (consonants.indexOf(word[i]) != -1) {
      if (i == word.length - 1) {
        return "";
      } else {
        if (vowels.indexOf(word[i + 1]) != -1) {
          return word[i + 1];
        }
      }
    }
    i--;
  }

  return "";
}



