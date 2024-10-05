  var result = '';
  var alphabet = 'abcdefghijklmnopqrstuvwxyz';
  var shift = 4;

  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    let index = alphabet.indexOf(c);
    if (index >= 0) {
      let new_index = (index + shift) % 26;
      result += alphabet[new_index];
    } else {
      result += c;
    }
  }

  return result;
}



