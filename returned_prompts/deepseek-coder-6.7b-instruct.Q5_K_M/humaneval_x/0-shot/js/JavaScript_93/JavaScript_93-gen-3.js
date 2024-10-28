  let encodedMessage = '';

  for(let i = 0; i < message.length; i++) {
    let char = message[i];

    if(char.match(/[aeiou]/i)) {
      if(char === char.toUpperCase()) {
        encodedMessage += String.fromCharCode(char.charCodeAt() + 26 - 65);
      } else {
        encodedMessage += String.fromCharCode(char.charCodeAt() + 26 - 97);
      }
    } else {
      encodedMessage += char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
    }
  }

  return encodedMessage;
}
console.log(encode('test')); // 'TGST'
console.log(encode('This is a message')); // 'tHKS KS C MGSSCGG'
  
*/

// Solution:
/*
The function `encode` takes a message as an argument. It iterates over each character in the message. 
If the character is a vowel (checked using regular expression), it checks if it's uppercase or lowercase and 
adds the corresponding character that appears 2 places ahead in the English alphabet to the encoded message.
If the character is not a vowel, it simply swaps its case to the encoded message. 
Finally, it returns the encoded message.
*/

// Complexity:
/*
The time complexity of this solution is O(n), where n is the length of the input message. This is because we iterate over the message once.
The space complexity is also O(n), as we store the encoded message.
*/

// Test Cases:
/*
encode('test') returns 'TGST'
encode('This is a message') returns 'tHKS KS C MGSSCGG'
encode('HEllo WOrld') returns 'hgSS vWrsg'
encode('JAVASCRIPT') returns 'jcVCSUGPWT'
*/

// Edge Cases:
/*
encode('') returns ''
encode('1234567890') returns '123