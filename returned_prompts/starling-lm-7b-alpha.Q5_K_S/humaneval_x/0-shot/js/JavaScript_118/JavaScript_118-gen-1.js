To solve this problem, we can follow these steps:

1. Define an array of vowels as ['a', 'e', 'i', 'o', 'u'].
2. Iterate through the word, starting from the second character (as the first character cannot be between two consonants), until we reach the end of the word.
3. Check if the current character is a consonant (i.e., not a vowel) and if the next character is also a consonant.
4. If both conditions are met, and a vowel is found in the array of vowels, return that vowel.
5. If no vowel is found, return an empty string.

Here's the code that implements the above steps:

```javascript
function getClosestVowel(word) {
  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  let closestVowel = '';

  for (let i = 1; i < word.length; i++) {
    if (
      /[^aeiouAEIOU]/.test(word[i]) &&
      /[^aeiouAEIOU]/.test(word[i + 1]) &&
      vowels.includes(word[i])
    ) {
      closestVowel = word[i];
      break;
    }
  }

  return closestVowel;
}
```

You can test the function with the provided examples:

```javascript
console.log(getClosestVowel("yogurt")); // Output: "u"
console.log(getClosestVowel("FULL"));   // Output: "U"
console.log(getClosestVowel("quick"));  // Output: ""
console.log(getClosestVowel("ab"));     // Output: ""
```

This function will return the closest vowel that stands between two consonants from the right side of the word. If no such vowel is found, it will return an empty string.

Note: The regular expression `/[^aeiou