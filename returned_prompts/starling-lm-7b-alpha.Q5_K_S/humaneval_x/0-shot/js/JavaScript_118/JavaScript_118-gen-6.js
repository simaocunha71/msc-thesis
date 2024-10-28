  // find the consonants and vowels
  const consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
  const vowels = "aeiouAEIOU";

  let left = 0;
  let right = word.length - 1;

  // if the first letter is vowel, return ""
  while (left < right && vowels.includes(word[left])) {
    left++;
  }

  // if the last letter is a vowel, return ""
  while (left < right && vowels.includes(word[right])) {
    right--;
  }

  // check if the string is empty or contains only vowels or consonants
  if (left >= right) {
    return "";
  }

  let minDistance = Number.MAX_SAFE_INTEGER;
  let result = "";

  // find the closest vowel
  while (left < right) {
    if (consonants.includes(word[left - 1]) && consonants.includes(word[right + 1])) {
      if (vowels.includes(word[left]) && Math.min(left, right) < minDistance) {
        minDistance = Math.min(left, right);
        result = word[minDistance];
      } else if (vowels.includes(word[right]) && Math.max(left, right) > minDistance) {
        minDistance = Math.max(left, right);
        result = word[minDistance];
      }
    }
    left++;
    right--;
  }

  return result;
};

console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""

*/




























