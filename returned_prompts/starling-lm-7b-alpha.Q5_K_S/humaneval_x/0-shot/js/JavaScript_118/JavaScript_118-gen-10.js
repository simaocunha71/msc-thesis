
const vowels = "aeiou";
const vowelIndices = [];

for (let i = 0; i < word.length; i++) {
  if (vowels.includes(word[i])) {
    vowelIndices.push(i);
  }
}

if (vowelIndices.length === 0) {
  return "";
}

const firstVowelIndex = vowelIndices[0];
const lastVowelIndex = vowelIndices[vowelIndices.length - 1];

if (word.charAt(firstVowelIndex - 1) === word.charAt(firstVowelIndex + 1)) {
  return word.charAt(lastVowelIndex + 1);
} else if (word.charAt(lastVowelIndex - 1) === word.charAt(lastVowelIndex + 1)) {
  return word.charAt(firstVowelIndex - 1);
} else {
  const firstDistance = firstVowelIndex - word.charAt(firstVowelIndex - 1)
    .charCodeAt()
    .toString();
  const lastDistance = lastVowelIndex - word.charAt(lastVowelIndex - 1)
    .charCodeAt()
    .toString();
  return firstDistance < lastDistance ? word.charAt(firstVowelIndex) : word.charAt(lastVowelIndex);
}
};

// Test
console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""



*/
















































































