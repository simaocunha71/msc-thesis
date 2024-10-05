  const vowels = ['a','e','i','o','u'];
  const messageArray = message.toLowerCase().split('');
  const result = [];

  messageArray.forEach(letter => {
    if (vowels.includes(letter)) {
      const index = vowels.indexOf(letter);
      result.push(vowels[(index + 2) % vowels.length]);
    } else if (letter !== ' ') {
      result.push(letter === 'z' ? 'a' : letter.charCodeAt(0) + 1);
    } else {
      result.push(' ');
    }
  });

  return result.join('');
};

/*
  Decode a message that was encoded using the same rules as above. 
  The decoding rules are the opposite of the encoding rules.
  Assume only letters.
  
  >>> decode('tHKS KS C MGSSCGG')
  'This is a message'
  >>> decode('TGST')
  'test'
  */
const decode = (message) => {
  const vowels = ['a','e','i','o','u'];
  const messageArray = message.toLowerCase().split('');
  const result = [];

  messageArray.forEach(letter => {
    if (vowels.includes(letter)) {
      const index = vowels.indexOf(letter);
      result.push(vowels[(index - 2 + vowels.length) % vowels.length]);
    } else if (letter !== ' ') {
      result.push(letter === 'a' ? 'z' : String.fromCharCode(letter.charCodeAt(0) - 1));
    } else {
      result.push(' ');
    }
  });

  return result.join('');
};

module.exports = {
  encode,
  decode
};

*/


























































