  const vowel = ["a", "e", "i", "o", "u"];
  const consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];
  const wordArray = word.split('');

  for (let i = 1; i < wordArray.length - 1; i++) {
    if (consonant.includes(wordArray[i]) && consonant.includes(wordArray[i + 1])) {
      for (const v of vowel) {
        if (v == wordArray[i + 1]) {
          return wordArray[i + 1];
        }
      }
    }
  }

  return '';
}



