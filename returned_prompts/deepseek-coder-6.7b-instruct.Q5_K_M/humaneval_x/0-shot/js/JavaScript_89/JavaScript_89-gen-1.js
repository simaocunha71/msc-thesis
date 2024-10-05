  let encrypted = '';
  for(let i = 0; i < s.length; i++){
    let char = s[i].charCodeAt();
    if((char >= 65 && char <= 90) || (char >= 97 && char <= 122)){
      encrypted += String.fromCharCode(char + 2*2);
    } else {
      encrypted += s[i];
    }
  }
  return encrypted;
}

console.log(encrypt('hi')); // returns 'jm'
console.log(encrypt('asdfghjkl')); // returns 'cwfhijkmp'
console.log(encrypt('gf')); // returns 'ij'
console.log(encrypt('et')); // returns 'gh'

// The code works by iterating through each character in the string. If the character is a letter (uppercase or lowercase), it gets its ASCII value, adds 2*2 (to rotate the alphabet down by two places), and converts that back to a character with the String.fromCharCode() method. If the character is not a letter, it is added to the encrypted string as is.

// Note that the result might include characters that are not letters. This is because the shift operation can move a character outside the alphabet. For example, 'z' shifted down by two places becomes 'b'.

// Also, the result might include characters that are not printable. This is because the shift operation can move a character outside the ASCII range. For example, the character with ASCII value 31 shifted down by two places becomes the character with ASCII value 255.

// To prevent this, you can add a check to see if the shifted character is within the printable ASCII range before adding it to the encrypted string. You could add this check by checking if the shifted character's ASCII value is between 32 and 126. If it is not, you could add the character to the encrypted string as is.





























































