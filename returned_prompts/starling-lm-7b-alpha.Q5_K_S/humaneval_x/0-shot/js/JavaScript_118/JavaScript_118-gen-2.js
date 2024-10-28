let vowels = ["a", "e", "i", "o", "u"];
let closest = "";
let index = -1;

for (let i = 1; i < word.length - 1; i++) {
  if (vowels.includes(word[i])) {
    index = i;
    break;
  }
}

if (index === -1) return "";

let prevCons = word[index - 1];
let nextCons = word[index + 1];

if (prevCons.toLowerCase() === "x" || prevCons.toLowerCase() === "z") {
  if (index === 0) {
    return "";
  }
  prevCons = word[index - 2];
}

if (nextCons.toLowerCase() === "x" || nextCons.toLowerCase() === "z") {
  if (index === word.length - 1) {
    return "";
  }
  nextCons = word[index + 2];
}

for (let vowel of vowels) {
  if (
    vowel.toLowerCase() !== prevCons.toLowerCase() &&
    vowel.toLowerCase() !== nextCons.toLowerCase()
  ) {
    closest = vowel;
    break;
  }
}

return closest;
};

// Tests
console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""
console.log(getClosestVowel("axax")); // "a"
console.log(getClosestVowel("axay")); // "a"
console.log(getClosestVowel("ayax")); // "a"
console.log(getClosestVowel("ayax")); // "a"
console.log(getClosestVowel("ayax")); // "a"
console.log(getClosestVowel("ayax")); // "a"
console.log(