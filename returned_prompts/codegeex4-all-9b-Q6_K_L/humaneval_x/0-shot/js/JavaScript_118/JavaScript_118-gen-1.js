const getClosestVowel = (word) => {
  const vowels = 'aeiouAEIOU';
  const wordArr = word.split('');
  
  for (let i = wordArr.length - 1; i > 0; i--) {
    const currentChar = wordArr[i];
    const nextChar = wordArr[i - 1];
    
    if (vowels.includes(currentChar) && !vowels.includes(nextChar)) {
      return currentChar;
    }
  }
  
  return '';
};

// Test cases
console.log(getClosestVowel("yogurt")); // "u"
console.log(getClosestVowel("FULL")); // "U"
console.log(getClosestVowel("quick")); // ""
console.log(getClosestVowel("ab")); // ""