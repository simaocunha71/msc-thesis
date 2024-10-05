  const vowels = "AEIOUaeiou";
  const consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz";
  let vowelIndexes = [];
  let consonantIndexes = [];

  for (let i = word.length - 1; i >= 1; i--) {
    if (vowels.includes(word[i])) {
      vowelIndexes.push(i);
    } else if (consonants.includes(word[i])) {
      consonantIndexes.push(i);
    }
  }
  
  for (let i = 0; i < vowelIndexes.length; i++) {
    if (vowelIndexes[i + 1] - vowelIndexes[i] > 1) {
      return word[vowelIndexes[i]];
    }
  }
  
  return "";
}
```

This function works by iterating through the word from right to left. It checks each character to see if it is a vowel or consonant and adds its index to the appropriate array. Then, it iterates through the array of vowel indexes, checking the difference between each adjacent vowel index. If the difference is more than 1, it returns the vowel at the previous index. If no such vowel exists, it returns an empty string.

The time complexity of this function is O(n), where n is the length of the word, because it iterates through the word once to collect the indexes of the vowels and consonants, and then iterates through the array of vowel indexes once to find the closest vowel. The space complexity is also O(n), because it uses two arrays to store the indexes of the vowels and consonants.

Note: The problem statement is a bit ambiguous, so it's assumed that the word only contains English letters. If the word can contain non-English letters, the function would need to be adjusted accordingly.

Note: This function assumes that the input word has at least two characters. If the word has less than two characters, the function will return an empty string.

Note: The function is case-sensitive. If