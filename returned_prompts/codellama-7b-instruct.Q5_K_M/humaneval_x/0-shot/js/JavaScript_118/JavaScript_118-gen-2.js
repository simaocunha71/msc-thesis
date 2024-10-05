  const vowels = ["a", "e", "i", "o", "u"];
  const consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];
  const wordArr = word.split("");
  let closestVowel = "";
  let closestVowelIndex = 0;

  for (let i = word.length - 1; i > 0; i--) {
    if (consonants.includes(wordArr[i]) && vowels.includes(wordArr[i - 1])) {
      closestVowel = wordArr[i - 1];
      closestVowelIndex = i - 1;
      break;
    }
  }

  if (closestVowel === "") {
    for (let i = 1; i < word.length; i++) {
      if (consonants.includes(wordArr[i]) && vowels.includes(wordArr[i - 1])) {
        closestVowel = wordArr[i - 1];
        closestVowelIndex = i - 1;
        break;
      }
    }
  }

  if (wordArr[0] === closestVowel) {
    return "";
  } else {
    return closestVowel;
  }
};
