```
const getClosestVowel = (word) => {
  const vowels = 'aeiouAEIOU';
  for (let i = word.length - 1; i > 0; i--) {
    if (vowels.includes(word[i])) {
      for (let j = i - 1; j >= 0; j--) {
        if (!vowels.includes(word[j])) {
          return word[j];
        }
      }
    }
  }
  return '';
};
```


Explanation:
- We iterate through the word from right to left using a for loop.
- For each character, we check if it's a vowel by using the includes method on the vowels string.
- If it's a vowel, we then iterate through the previous characters (from left to right) to find the closest consonant.
- When we find a consonant, we return that character.
- If no vowel is found between two consonants, we return an empty string.

Note: This solution assumes that the input word only contains English letters. If the input word can contain non-English characters, additional checks may be necessary.