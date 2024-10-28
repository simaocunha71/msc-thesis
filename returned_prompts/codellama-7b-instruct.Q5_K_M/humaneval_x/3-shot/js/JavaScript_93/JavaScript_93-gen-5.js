  let encodedMessage = '';
  
  for (let i = 0; i < message.length; i++) {
    let letter = message[i];

    if (letter === letter.toUpperCase()) {
      encodedMessage += letter.toLowerCase();
    } else {
      encodedMessage += letter.toUpperCase();
    }

    if (letter === 'a' || letter === 'e' || letter === 'i' || letter === 'o' || letter === 'u') {
      let index = letter.charCodeAt(0) - 97;
      let nextLetter = String.fromCharCode(index + 2);
      encodedMessage += nextLetter;
    }
  }

  return encodedMessage;
}



