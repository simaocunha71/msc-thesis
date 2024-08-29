  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  let lastConsonant = word[word.length - 1];
  let secondLastConsonant = word[word.length - 2];
  let closestVowel = '';
  for (let i = word.length - 1; i >= 0; i--) {
    if (vowels.includes(word[i])) {
      if (word[i + 1] === lastConsonant && word[i - 1] === secondLastConsonant) {
        closestVowel = word[i];
        break;
      } else if (word[i + 1] === lastConsonant) {
        closestVowel = word[i];
      } else if (word[i - 1] === secondLastConsonant) {
        closestVowel = word[i];
      }
    }
  }
  return closestVowel;
}



