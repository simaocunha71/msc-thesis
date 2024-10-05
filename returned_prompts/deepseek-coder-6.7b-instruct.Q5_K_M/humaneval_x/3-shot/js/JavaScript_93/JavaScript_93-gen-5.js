  let encodedMessage = '';
  let vowels = ['a', 'e', 'i', 'o', 'u'];

  for (let i = 0; i < message.length; i++) {
    let char = message[i];

    if (char.match(/[a-z]/i)) {
      if (vowels.includes(char.toLowerCase())) {
        encodedMessage += String.fromCharCode(char.charCodeAt(0) + 2);
      } else {
        encodedMessage += char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
      }
    } else {
      encodedMessage += char;
    }
  }

  return encodedMessage;
}



