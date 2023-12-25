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
  let arr = s.split("");
  let rv = "", l, c;
  
    for(let i = 0; i < arr.length; i++) {
      if ((i + 1) % 2 === 0 && l >= "e" || l >= "a")
        c = (l - "e").toLowerCase();
      else if((i + 1) % 2 === 1 && l >= "f".toLowerCase())
        c = "kj";
      rv += c;
      l = arr[i + 1];
    }
   return rv;
}