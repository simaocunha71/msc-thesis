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
  let index, closestIndex;
  for(let i = 2; i < word.length - 1;i++){
    if(
      !/\w/.test(word[i]) &&
      !/[aeiou]/g.test(word[i + 1]))) {
      continue;
    } else {
      index = i;
      closestIndex = i - 1;
    }
    
    if(/[aeiou]/g.test(word[index])) {
      return word[index];
    } else {
      break;
    }
  }
};