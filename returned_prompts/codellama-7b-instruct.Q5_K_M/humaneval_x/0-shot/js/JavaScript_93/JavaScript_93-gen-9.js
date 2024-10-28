/*
  Write a function that takes a message, and encodes in such a 
  way that it swaps case of all letters, replaces all vowels in 
  the message with the letter that appears 2 places ahead of that 
  vowel in the english alphabet. 
  Assume only letters. 
  
  Examples:
  >>> encode('test')
  'TGST'
  >>> encode('This is a message')
  'tHKS KS C MGSSCGG'
  */
const encode = (message) => {
  let encodedMsg = '';
  for (let i = 0; i < message.length; i++) {
    const char = message[i];
    if (char.match(/[a-z]/i)) {
      encodedMsg += char.match(/[a-z]/i) ? 
      String.fromCharCode(char.charCodeAt(0) + 2) : 
      String.fromCharCode(char.charCodeAt(0) - 2);
    } else if (char.match(/[A-Z]/)) {
      encodedMsg += char.match(/[A-Z]/i) ?
      String.fromCharCode(char.charCodeAt(0) - 2) :
      String.fromCharCode(char.charCodeAt(0) + 2);
    } else {
      encodedMsg += char;
    }
  }
  return encodedMsg;
}



