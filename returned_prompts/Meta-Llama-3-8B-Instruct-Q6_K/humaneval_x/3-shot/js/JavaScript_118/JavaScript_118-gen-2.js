  let result = '';
  for (let i = word.length - 1; i > 0; i--) {
    if (/^[aeiouAEIOU]$/.test(word[i])) {
      for (let j = i - 1; j >= 0; j--) {
        if (/^[bcdfghjklmnpqrstBCDFGHJKLMNPQRST]$/.test(word[j])) {
          result = word[i];
          break;
        }
      }
      return result;
    }
  }
  return '';
}
// test cases
console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""
console.log(getClosestVowel("aeiou")); // ""
console.log(getClosestVowel("bcdfghjklmnpqrst")); // ""
console.log(getClosestVowel("")); // ""



