const encode = (message) => {
  const vowels = 'aeiou';
  const vowelMap = {
    a: 'A',
    e: 'E',
    i: 'I',
    o: 'O',
    u: 'U'
  };

  let encodedMessage = '';

  for (const char of message) {
    const isVowel = vowels.includes(char);

    if (isVowel) {
      encodedMessage += vowelMap[char];
    } else {
      const charCode = char.charCodeAt();

      if (charCode >= 65 && charCode <= 90) {
        encodedMessage += String.fromCharCode(charCode + 2);
      } else {
        encodedMessage += char;
      }
    }
  }

  return encodedMessage;
};
