  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let rotatedAlphabet = alphabet.slice(2 * 2 % 26,).concat(alphabet.slice(0, 2 * 2 % 26));
  let encrypted = '';
  for (let char of s.toLowerCase()) {
    if (char === ' ') {
      encrypted += ' ';
    } else {
      let index = alphabet.indexOf(char);
      encrypted += rotatedAlphabet[index];
    }
  }
  return encrypted;
}