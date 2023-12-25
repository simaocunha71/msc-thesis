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
    let swappedLetters = [];
    for (let i in message.toLowerCase()) {
      if(message[i].toUpperCase() === message[i]){
        swappedLetters.push(`${message[i]}`);
      }else{
          swappedLetters.push(`${message[i]} ${message[`${i + 1}`.toLowerCase()}]`);
      }
    }
    return swappedLetters;
};
