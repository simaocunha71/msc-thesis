  const vowels = 'aeiouAEIOU';
  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  let closestVowel = '';

  for (let i = word.length - 2; i > 0; i--) {
    if (consonants.includes(word[i]) && consonants.includes(word[i - 1]) && vowels.includes(word[i + 1])) {
      closestVowel = word[i + 1];
      break;
    }
  }

  return closestVowel;
};

console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""

*/


//Explanation:
In the given problem, we need to find the closest vowel that stands between two consonants from the right side of the word. We iterate the word from right to left, checking if the character at index i is a vowel and if the characters at index i-1 and i+1 are consonants. If these conditions are met, we assign the character at index i+1 to closestVowel and break the loop.

In the end, we return closestVowel which contains the closest vowel that meets the given conditions or an empty string if no such vowel is found.

*/






































































































































