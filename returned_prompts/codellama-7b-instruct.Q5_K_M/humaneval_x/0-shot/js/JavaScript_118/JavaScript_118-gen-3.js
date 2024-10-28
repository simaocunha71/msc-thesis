const getClosestVowel = (word) => {
  const vowels = ["a", "e", "i", "o", "u"];
  const wordArray = word.split("");
  let closestVowel = "";
  let previousVowel = "";

  for (let i = wordArray.length - 1; i >= 0; i--) {
    const currentChar = wordArray[i];
    if (vowels.includes(currentChar)) {
      if (previousVowel !== "") {
        closestVowel = currentChar;
      }
      previousVowel = currentChar;
    }
  }

  return closestVowel;
}

