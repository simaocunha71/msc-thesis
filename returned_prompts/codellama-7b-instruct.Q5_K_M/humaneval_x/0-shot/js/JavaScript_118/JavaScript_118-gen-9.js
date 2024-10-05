const getClosestVowel = (word) => {
  // Get the index of the last consonant and the first vowel
  const lastConsonantIndex = word.lastIndexOf(/[bcdfghjklmnpqrstvwxyz]/);
  const firstVowelIndex = word.indexOf(/[aeiou]/);

  // Check if there are consonants before or after the vowels
  if (lastConsonantIndex === -1 || firstVowelIndex === -1) {
    return "";
  }

  // Get the position of the closest vowel
  const closestVowelIndex = Math.abs(lastConsonantIndex - firstVowelIndex) < Math.abs(lastConsonantIndex - firstVowelIndex + 1) ? lastConsonantIndex : firstVowelIndex;

  // Return the closest vowel
  return word[closestVowelIndex];
};

B:
const getClosestVowel = (word) => {
  let lastConsonantIndex = -1;
  let firstVowelIndex = -1;
  let closestVowelIndex = -1;

  // Find the last consonant and the first vowel
  for (let i = word.length - 1; i >= 0; i--) {
    if (/[bcdfghjklmnpqrstvwxyz]/.test(word[i])) {
      lastConsonantIndex = i;
    }
    if (/[aeiou]/.test(word[i])) {
      firstVowelIndex = i;
    }
  }

  // Find the closest vowel
  if (lastConsonantIndex >= 0 && firstVowelIndex >= 0) {
    closestVowelIndex = Math.abs(lastConsonantIndex - firstVowelIndex) < Math.abs(lastConsonantIndex - firstVowelIndex + 1) ? lastConsonantIndex : firstVowelIndex;
  }

  // Return the closest vowel
  return closestVowelIndex >= 0 ? word[closestVowelIndex] : "";
};

C:
const getClosestVowel = (word) =>