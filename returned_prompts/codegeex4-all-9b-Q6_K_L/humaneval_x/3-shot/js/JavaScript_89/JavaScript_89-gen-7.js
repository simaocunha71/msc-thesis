  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let rotated_alphabet = alphabet.slice(4) + alphabet.slice(0, 4);
  let result = '';
  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    let index = alphabet.indexOf(c);
    result += rotated_alphabet[index];
  }
  return result;
}



