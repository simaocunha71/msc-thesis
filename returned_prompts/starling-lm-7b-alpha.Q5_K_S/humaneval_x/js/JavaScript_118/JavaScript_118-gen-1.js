  let vowel = "aeiou";
  let consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
  let result = "";

  for (let i = 0; i < word.length; i++) {
    if (vowel.includes(word[i])) {
      result = word[i];
    } else if (consonant.includes(word[i])) {
      if (i < word.length - 1 && vowel.includes(word[i + 1])) {
        result = word[i + 1];
      } else if (i > 0 && vowel.includes(word[i - 1])) {
        result = word[i - 1];
      }
    }
  }

  return result;
}



