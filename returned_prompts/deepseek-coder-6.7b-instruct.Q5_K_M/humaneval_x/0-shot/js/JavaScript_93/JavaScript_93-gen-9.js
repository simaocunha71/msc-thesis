  let encodedMessage = '';
  
  for(let i = 0; i < message.length; i++){
    let char = message[i];
    
    if(char.match(/[aeiou]/i)){
      encodedMessage += String.fromCharCode(char.charCodeAt(0) + 2);
    } else if(char === char.toUpperCase()){
      encodedMessage += char.toLowerCase();
    } else {
      encodedMessage += char.toUpperCase();
    }
  }
  
  return encodedMessage;
};

console.log(encode('test'));
console.log(encode('This is a message'));
console.log(encode('Aeiou'));
console.log(encode('Hello World'));
console.log(encode('Javascript'));

module.exports = encode;

This function starts by initializing an empty string `encodedMessage`. It then loops through each character in the message. If the character is a vowel (matched using a regular expression), it finds the character that appears 2 places ahead in the alphabet using `char.charCodeAt(0) + 2` and adds it to `encodedMessage`. If the character is uppercase, it converts it to lowercase and adds it to `encodedMessage`, and if it's lowercase, it converts it to uppercase and adds it to `encodedMessage`. Finally, it returns `encodedMessage`.

The regular expression `/[aeiou]/i` matches any vowel (either upper or lower case). The `charCodeAt(0)` method returns the Unicode of the character, and adding 2 to it gives us the Unicode of the character that appears 2 places ahead. `String.fromCharCode()` is used to convert this Unicode back into a character.

The `toUpperCase()` and `toLowerCase()` methods are used to convert characters to uppercase and lowercase respectively.

The function handles both vowels and non-vowels by checking if the character is a vowel and if it is uppercase, then converting it to lowercase. If it's not a vowel and is lowercase, it converts it to uppercase.
*/
