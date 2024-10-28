const encode = (message) => {
  let encodedMessage = '';
  for (let i = 0; i < message.length; i++) {
    const char = message[i];
    if (char.match(/[a-zA-Z]/)) {
      if (char.match(/[a-z]/)) {
        encodedMessage += char.toUpperCase();
      } else {
        const newChar = char.toLowerCase();
        const vowel = char.charCodeAt() - 97;
        const newVowel = vowel + 2;
        encodedMessage += String.fromCharCode(newVowel + 97);
      }
    } else {
      encodedMessage += char;
    }
  }
  return encodedMessage;
}

console.log(encode('This is a message'))