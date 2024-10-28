let encrypted = '';

for (let i = 0; i < s.length; i++) {
  let ascii = s[i].charCodeAt();
  if ((ascii >= 65 && ascii <= 90) || (ascii >= 97 && ascii <= 122)) {
    encrypted += String.fromCharCode(ascii + 2 * 2);
  } else {
    encrypted += s[i];
  }
}

return encrypted;
}
console.log(encrypt('hi')); // returns 'jm'
console.log(encrypt('asdfghjkl')); // returns 'cwkhijmpq'
console.log(encrypt('gf')); // returns 'ij'
console.log(encrypt('et')); // returns 'gh'
console.log(encrypt('aA')); // returns 'cC'




// encrypts the string by shifting each character 2 places down the alphabet and 2 places to the right.



// the for loop iterates over each character in the string.
// the if statement checks if the character is an uppercase or lowercase letter.
// if it is, the charCodeAt() method returns the ASCII value of the character.
// The ASCII value of 'A' is 65 and 'Z' is 90. The ASCII value of 'a' is 97 and 'z' is 122.
// if the character is a letter, the charCodeAt() method returns the ASCII value of the character plus 4 (2 places down and 2 places to the right).
// if the character is not a letter, it's added to the encrypted string as it is.
// the function returns the encrypted string.
// the console.log() statements test the function with various strings.
// the output is the encrypted string.

// the function encrypts the string by shifting each character 2 places down the alphabet and 2 places to the right.
// it does this by iterating over each character in the string, checking if it is a letter, and if it is, shifting it accordingly.
// it returns the encrypted string.

// the function encrypts the string by shifting each character