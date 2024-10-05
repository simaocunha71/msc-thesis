/*
  checkIfLastCharIsALetter("apple pie") ➞ false
  checkIfLastCharIsALetter("apple pi e") ➞ true
  checkIfLastCharIsALetter("apple pi e ") ➞ false
  checkIfLastCharIsALetter("") ➞ false
  */
const checkIfLastCharIsALetter = (txt) => {

  const lastChar = txt.charAt(txt.length - 1);
  const lastWord = txt.split(" ").pop();
  console.log(lastWord, lastChar);
  const lastIsAWord = lastWord.includes(lastChar);
  console.log(lastIsAWord);
  return lastIsAWord ? false : true;
}



