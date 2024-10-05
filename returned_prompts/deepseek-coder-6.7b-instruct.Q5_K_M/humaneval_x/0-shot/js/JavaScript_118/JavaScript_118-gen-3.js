  const vowels = 'aeiouAEIOU';
  for (let i = word.length - 2; i > 0; i--) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i - 1]) && !vowels.includes(word[i + 1])) {
      return word[i];
    }
  }
  return '';
};

console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""

// Tests:
console.log(getClosestVowel("yogurt") === "u");
console.log(getClosestVowel("FULL") === "U");
console.log(getClosestVowel("quick") === "");
console.log(getClosestVowel("ab") === "");
console.log(getClosestVowel("coder") === "e");
console.log(getClosestVowel("FLOWER") === "O");
console.log(getClosestVowel("JS") === "");
console.log(getClosestVowel("") === "");

```

```python
# Python
