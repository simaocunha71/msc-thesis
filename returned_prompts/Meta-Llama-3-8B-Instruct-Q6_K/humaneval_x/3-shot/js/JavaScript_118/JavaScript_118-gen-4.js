  let result = '';
  let left = 0;
  let right = word.length - 1;

  while (left < right) {
    if (isVowel(word[left])) {
      left++;
    } else if (isVowel(word[right])) {
      result = word.slice(right, right + 1);
      return result;
    } else {
      right--;
    }
  }

  function isVowel(c) {
    return 'aeiouAEIOU'.indexOf(c) !== -1;
  }

  return result;
}
//Test cases:
console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""
console.log(getClosestVowel("hello")); // "o"
console.log(getClosestVowel("world")); // "o"
console.log(getClosestVowel("aeiou")); // ""
console.log(getClosestVowel("bcdfghjklmnpqrstvwxyz")); // ""



