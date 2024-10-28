const removeVowels = (text) => {
  // The string to return
  let result = '';
  // Iterate through each character in the input string
  for (let i = 0; i < text.length; i++) {
    // If the current character is a vowel, skip it
    if (['a', 'e', 'i', 'o', 'u'].includes(text[i].toLowerCase())) {
      continue;
    }
    // If the current character is not a vowel, add it to the result string
    result += text[i];
  }
  // Return the result string
  return result;
}

/* Uncomment to test code
console.log(removeVowels('')); // ''
console.log(removeVowels('abcdef\nghijklm')); // 'bcdf\nghjklm'
console.log(removeVowels('abcdef')); // 'bcdf'
console.log(removeVowels('aaaaa')); // ''
console.log(removeVowels('aaBAA')); // 'B'
console.log(removeVowels('zbcd')); // 'zbcd'
*/