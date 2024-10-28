/*
  "apple pie" ➞ false
  "apple pi e" ➞ true
  "apple pi e " ➞ false
  "" ➞ false
*/
const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt.slice(-1);
  if (!lastChar.match(/[a-zA-Z]/)) {
    return false;
  }
  if (lastChar.match(/[a-zA-Z]/g).length !== 1) {
    return false;
  }
  return true;
};





