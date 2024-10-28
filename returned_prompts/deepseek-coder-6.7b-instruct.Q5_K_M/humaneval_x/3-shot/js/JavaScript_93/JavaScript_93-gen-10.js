  let encodedMessage = '';
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  
  for(let i = 0; i < message.length; i++) {
    let char = message[i];
    if(char.match(/[a-z]/i)) {
      if(vowels.includes(char.toLowerCase())) {
        encodedMessage += String.fromCharCode(char.charCodeAt(0) + 2);
      } else {
        encodedMessage += char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase();
      }
    } else {
      encodedMessage += char;
    }
  }
  return encodedMessage;
}



