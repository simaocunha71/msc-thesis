  let result = [];
  let consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

  const isConsonant = (c) => {
    return consonants.includes(c);
  };

  for (let i = 0; i < s.length; i++) {
    let count = 0;
    let currentWord = "";
    while (i < s.length && s[i] != ' ') {
      currentWord += s[i++];
      if (isConsonant(s[i])) {
        count++;
      }
    }
    if (count === n) {
      result.push(currentWord);
    }
  }

  return result;
}



