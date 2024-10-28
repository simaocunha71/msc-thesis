  const vowels = 'AEIOUaeiou';
  const consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz';
  let result = '';

  for(let i = word.length - 2; i > 0; i--) {
    if(consonants.includes(word[i]) && consonants.includes(word[i+1]) && vowels.includes(word[i-1])) {
      result = word[i-1];
      break;
    }
  }

  return result;
}

console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""
console.log(getClosestVowel("AEIOU")); // ""
console.log(getClosestVowel("abcde")); // ""
console.log(getClosestVowel("bcdfg")); // ""
console.log(getClosestVowel("BcDfG")); // "c"
console.log(getClosestVowel("YogUrt")); // "U"
console.log(getClosestVowel("FuLl")); // "U"
console.log(getClosestVowel("quIck")); // ""
console.log(getClosestVowel("abCdE")); // "b"
console.log(getClosestVowel("bCdFg")); // "C"
console.log(getClosestVowel("BCDFG")); // ""
console.log(getClosestVowel("12345")); // ""
console.log(getClosestVowel("abc123")); // "b"
console.log(getClosestVowel("bcd234")); // "c"
console.log(getClosestVowel("BC