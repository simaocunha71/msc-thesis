  return s.split('').map(character => {
    let charCode = character.charCodeAt(0);
    if (charCode >= 65 && charCode <= 90) {
      return String.fromCharCode(((charCode - 65 + 2*2) % 26) + 65);
    } else if (charCode >= 97 && charCode <= 122) {
      return String.fromCharCode(((charCode - 97 + 2*2) % 26) + 97);
    } else {
      return character;
    }
  }).join('');
}

console.log(encrypt('hi')); // returns 'lm'
console.log(encrypt('asdfghjkl')); // returns 'ewhjklnop'
console.log(encrypt('gf')); // returns 'kj'
console.log(encrypt('et')); // returns 'ix'


/*
This function works by splitting the input string into an array of characters,
then mapping over the array with a function that transforms each character.
The transformation is based on the ASCII value of the character. If the character
is an uppercase or lowercase letter, it is transformed according to the rules
of a Caesar cipher with a shift of 2 places. If the character is not a letter,
it is returned unchanged.
*/





































































































































































































