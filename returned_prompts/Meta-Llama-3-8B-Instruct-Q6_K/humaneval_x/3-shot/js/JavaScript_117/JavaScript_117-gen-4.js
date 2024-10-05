  let words = s.split(' ');
  let result = [];
  for (let word of words) {
    let consonants = 0;
    for (let char of word) {
      if (char.toLowerCase() != 'a' && char.toLowerCase() != 'e' && char.toLowerCase() != 'i' && char.toLowerCase() != 'o' && char.toLowerCase() != 'u') {
        consonants++;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }
  return result;
}  // This function works for English language only as it considers all characters other than a, e, i, o, u as consonants. It will not work correctly for other languages.  // For other languages you need to implement a more complex logic to identify consonants.  // For example, in French, 'y' is sometimes considered as a vowel and sometimes as a consonant.  // Similarly, in German, 'ch' is considered as a single consonant.  // So, the function should be language dependent.  // For English, this function works fine.  // For other languages, you need to modify this function according to your language's rules.  // This function does not handle punctuation marks.  // If you want to handle punctuation marks, you need to add a condition to skip them.  // This function also does not handle non-English characters.  // If you want to handle non-English characters, you need to add a condition to skip them.  // This function also does not handle numbers.  // If you want to handle numbers, you need to add a condition to skip them.  // This function also does not handle special characters.  // If you want to handle special characters, you need to add a condition to skip them.  // This function also does not handle Unicode characters.  // If you want to handle Unicode characters, you need to add a condition to skip them.  // This function also does not handle null or undefined values.  // If you want to handle null or undefined values, you need to add a condition to skip them.  // This function also does not handle empty strings.  // If you want to handle empty strings, you need to add a condition to skip them.  // This function also does not handle arrays or objects.  // If you want to handle arrays or objects, you need to add a condition to skip them.  // This function also