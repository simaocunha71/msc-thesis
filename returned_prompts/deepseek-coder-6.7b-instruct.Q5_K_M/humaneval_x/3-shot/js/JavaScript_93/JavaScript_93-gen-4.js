  let encoded = '';
  const vowels = {'a':'c', 'e':'g', 'i':'k', 'o':'q', 'u':'w', 'A':'C', 'E':'G', 'I':'K', 'O':'Q', 'U':'W'};
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-z]/i)) {
      encoded += vowels[char] || char.toUpperCase();
    } else {
      encoded += char;
    }
  }
  return encoded;
}



