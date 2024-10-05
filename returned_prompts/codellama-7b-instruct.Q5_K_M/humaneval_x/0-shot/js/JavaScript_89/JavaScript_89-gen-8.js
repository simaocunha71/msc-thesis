/*Create a function encrypt that takes a string as an argument and
  returns a string encrypted with the alphabet being rotated. 
  The alphabet should be rotated in a manner such that the letters 
  shift down by two multiplied to two places.
  For example:
  encrypt('hi') returns 'lm'
  encrypt('asdfghjkl') returns 'ewhjklnop'
  encrypt('gf') returns 'kj'
  encrypt('et') returns 'ix'
  */
const encrypt = (s) => {
  let newString = '';
  for (let i = 0; i < s.length; i++) {
    let charCode = s.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) {
      newString += String.fromCharCode(((charCode - 65 + 2 * 2) % 26) + 65);
    } else if (charCode >= 97 && charCode <= 122) {
      newString += String.fromCharCode(((charCode - 97 + 2 * 2) % 26) + 97);
    } else {
      newString += s[i];
    }
  }
  return newString;
}

