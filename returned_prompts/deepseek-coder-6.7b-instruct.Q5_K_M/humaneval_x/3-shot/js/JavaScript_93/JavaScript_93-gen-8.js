  let encoded = '';
  const vowels = {'a':'c', 'e':'g', 'i':'k', 'o':'q', 'u':'w', 'A':'C', 'E':'G', 'I':'K', 'O':'Q', 'U':'W'};

  for (let i = 0; i < message.length; i++) {
    if (message[i] in vowels) {
      encoded += vowels[message[i]];
    } else {
      encoded += message[i] === message[i].toUpperCase() ? message[i].toLowerCase() : message[i].toUpperCase();
    }
  }

  return encoded;
}



