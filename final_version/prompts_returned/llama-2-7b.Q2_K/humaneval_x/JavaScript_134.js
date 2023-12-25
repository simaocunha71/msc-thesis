/* Create a function that returns true if the last character
  of a given string is an alphabetical character and is not
  a part of a word, and false otherwise.
  Note: "word" is a group of characters separated by space.
  Examples:
  checkIfLastCharIsALetter("apple pie") ➞ false
  checkIfLastCharIsALetter("apple pi e") ➞ true
  checkIfLastCharIsALetter("apple pi e ") ➞ false
  checkIfLastCharIsALetter("") ➞ false
  */
const checkIfLastCharIsALetter = (txt) => {
  if(txt.length === 0) return true; // empty word, empty string
  const lastAlphabeticalLetter = getLastLetterOfString(txt).toLowerCase();
  let isPartialWord = false;
  for(let i=lastAlphabeticalLetter.length-1;i>0;--i) { // loop through the alphabetical letters in reverse order, except if you are inside a word
    const charInString = getLastCharacterOfString(txt);
    if(charInString == lastAlphabeticalLetter[i]) isPartialWord = true; // charInString was contained within the string, so it wasn't an alphabetical character
  }
  return !isPartialWord && lastAlphabeticalLetter !== "" && lastAlphabeticalLetter.length > 0; // don't check word if alphabetical letter is empty and/or there isn't any alphabetical letters in the string anymore
};

/*
Checks if a string contains only vowels, spaces, and consonants (a-z or A-Z with space). Examples:
  checkIfStringIsOnlyAlphabeticalLetters(" apple") ➞ true
   checkIfStringIsOnlyAlphabeticalLetters("apple pie") ➞ false
*/
const checkIfStringIsOnlyALetter = (txt) => {
  return txt.length > 0 ? getLastLetterOfString(txt).toLowerCase().trim() === "" || getLastCharacterOfString(txt).toLowerCase().indexOf('a-z') !== -1 : false; //