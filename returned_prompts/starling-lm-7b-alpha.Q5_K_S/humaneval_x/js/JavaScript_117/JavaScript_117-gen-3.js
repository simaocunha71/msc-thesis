  let result = [];
  let consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz";

  for (let i = 0; i < s.length; i++) {
    let word = "";
    let count = 0;

    while (i < s.length && (consonants.indexOf(s[i]) == -1 || count == n)) {
      word += s[i];
      i++;
      if (s[i] == ' ') {
        count += consonants.indexOf(word[word.length - 1]) != -1 ? 1 : 0;
        word = "";
      }
    }

    if (count == n) {
      result.push(word);
    }
  }

  return result;
}



