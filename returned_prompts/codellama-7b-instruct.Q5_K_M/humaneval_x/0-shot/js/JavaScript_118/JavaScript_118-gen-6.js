/*You are given a word. Your task is to find the closest vowel that stands between 
  two consonants from the right side of the word (case sensitive).
  
  Vowels in the beginning and ending doesn't count. Return empty string if you didn't
  find any vowel met the above condition. 

  You may assume that the given string contains English letter only.

  Example:
  getClosestVowel("yogurt") ==> "u"
  getClosestVowel("FULL") ==> "U"
  getClosestVowel("quick") ==> ""
  getClosestVowel("ab") ==> ""
  */
const getClosestVowel = (word) => {
  let vowels = ['a', 'e', 'i', 'o', 'u'];
  let leftIndex = -1;
  let rightIndex = word.length;
  let leftChar = '';
  let rightChar = '';
  for (let i = word.length - 1; i >= 0; i--) {
    if (vowels.includes(word[i])) {
      leftIndex = i;
      leftChar = word[i];
      break;
    }
  }
  if (leftIndex == -1) {
    return '';
  }
  for (let j = word.length; j < word.length; j++) {
    if (vowels.includes(word[j])) {
      rightIndex = j;
      rightChar = word[j];
      break;
    }
  }
  if (rightIndex == word.length) {
    return '';
  }
  return rightChar;
};