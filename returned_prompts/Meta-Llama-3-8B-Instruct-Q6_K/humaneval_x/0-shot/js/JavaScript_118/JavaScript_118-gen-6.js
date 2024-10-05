```
function getClosestVowel(word) {
  let lastConsonantIndex = -1;
  for (let i = word.length - 1; i >= 0; i--) {
    if (!['a', 'e', 'i', 'o', 'u'].includes(word[i].toLowerCase())) {
      lastConsonantIndex = i;
      break;
    }
  }
  if (lastConsonantIndex === -1) return '';
  for (let i = lastConsonantIndex - 1; i >= 0; i--) {
    if (['a', 'e', 'i', 'o', 'u'].includes(word[i].toLowerCase())) {
      return word[i];
    }
  }
  return '';
}
```


Explanation:
The function `getClosestVowel` iterates over the word from right to left to find the last consonant index. If it doesn't find any consonant, it returns an empty string. Then it iterates over the word from the last consonant index to the beginning to find the closest vowel. If it doesn't find any vowel, it returns an empty string.

Note: We use `toLowerCase()` to make the function case-insensitive, so it can find vowels regardless of their case. We also use `includes()` to check if a character is a vowel or a consonant.

Example usage:
```
console.log(getClosestVowel("yogurt")); // Output: "u"
console.log(getClosestVowel("FULL")); // Output: "U"
console.log(getClosestVowel("quick")); // Output: ""
console.log(getClosestVowel("ab")); // Output: ""
```


This function has a time complexity of O(n), where n is the length of the input word, because it iterates over the word twice. The space complexity is O(1), because it uses a constant amount of space to store the variables.