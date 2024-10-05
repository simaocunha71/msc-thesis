const getClosestVowel = (word) => {
  const vowels = ["a", "e", "i", "o", "u"];
  const consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];

  let closestVowel;
  let closestVowelIndex = -1;
  let currentVowelIndex = -1;
  let closestConsonantIndex = -1;

  for (let i = 0; i < word.length; i++) {
    const letter = word[i];
    if (vowels.includes(letter)) {
      currentVowelIndex = i;
      if (closestVowelIndex === -1) {
        closestVowelIndex = i;
      }
    }
    if (consonants.includes(letter)) {
      closestConsonantIndex = i;
    }
  }

  if (closestConsonantIndex !== -1 && currentVowelIndex !== -1) {
    return word[currentVowelIndex];
  }

  return "";
};
