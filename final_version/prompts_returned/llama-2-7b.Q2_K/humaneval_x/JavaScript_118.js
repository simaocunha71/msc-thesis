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
  let res = '';
  for(let i=0;i<25;i++){
    if (word[i] && word.includes('e' + String.fromCharCode(97+i))){
      res+=String.fromCharCode(97+i);
    }
  }
   return res || '';
}
