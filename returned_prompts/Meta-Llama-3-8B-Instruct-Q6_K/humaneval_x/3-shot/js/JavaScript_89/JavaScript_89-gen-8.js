  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let shiftedAlphabet = alphabet.slice(2 * 2) + alphabet.slice(0, 2 * 2);
  let result = '';
  for (let char of s.toLowerCase()) {
    if (char === ' ') {
      result += ' ';
    } else {
      let index = alphabet.indexOf(char);
      if (index !== -1) {
        result += shiftedAlphabet[index];
      } else {
        result += char;
      }
    }
  }
  return result;
}