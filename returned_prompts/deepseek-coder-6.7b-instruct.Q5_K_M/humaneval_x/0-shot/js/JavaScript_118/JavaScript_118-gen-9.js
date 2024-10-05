  const vowels = 'aeiouAEIOU';
  for(let i = word.length - 2; i > 0; i--) {
    if(vowels.includes(word[i]) && !vowels.includes(word[i-1]) && !vowels.includes(word[i+1])) {
      return word[i];
    }
  }
  return '';
}

console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""

```

This function starts from the second last character of the word and goes up until it reaches the first character. It checks if the character is a vowel and if both its neighbors (left and right) are consonants. If it finds such a character, it returns that character. If it doesn't find any such character, it returns an empty string.

Please note that the function is case sensitive, so 'A' is considered as a vowel but 'a' is considered as a consonant.
```

```javascript
const getClosestVowel = (word) => {
  const vowels = 'aeiouAEIOU';
  for(let i = word.length - 2; i > 0; i--) {
    if(vowels.includes(word[i]) && !vowels.includes(word[i-1]) && !vowels.includes(word[i+1])) {
      return word[i];
    }
  }
  return '';
}

console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""
```

```javascript
const getClosestVowel = (word) => {
  const vowels = 'aeiouAEIO