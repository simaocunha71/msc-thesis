  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (c == ' ') {
      encrypted += ' ';
    } else {
      let index = alphabet.indexOf(c);
      index = (index + 4) % 26;
      encrypted += alphabet[index];
    }
  }
  return encrypted;
}



