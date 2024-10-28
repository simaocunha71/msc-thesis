  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  for (let i = word.length - 2; i > 0; i--) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i - 1]) && !vowels.includes(word[i + 1])) {
      return word[i];
    }
  }
  return "";
}

console.log(getClosestVowel("yogurt")) //==> "u"
console.log(getClosestVowel("FULL")) //==> "U"
console.log(getClosestVowel("quick")) //==> ""
console.log(getClosestVowel("ab")) //==> ""
```

This solution works by starting from the second last character and going towards the start of the word. For each character, it checks if it is a vowel (not included in the vowels array), and if the characters to its left and right are not vowels (also not included in the vowels array). If both conditions are met, it returns that character. If no such character is found after checking all characters, it returns an empty string.

The time complexity of this solution is O(n), where n is the length of the word. This is because in the worst case scenario, it may need to check every character in the word. The space complexity is O(1), as it only uses a constant amount of space to store the vowels array and the result string.

Please note that the function is case sensitive, so 'U' is not considered a vowel in the word "FULL".

This function assumes that the input word contains only English alphabets and does not contain any spaces or special characters. If the input contains such characters, it may not work as expected.

This function can be used in various scenarios where you need to find the closest vowel that stands between two consonants in a given word.

Test cases:
getClosestVowel("yogurt") ➞ "u"
getClosestVowel("FULL") ➞ "U"