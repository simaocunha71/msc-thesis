  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const rotated_alphabet = alphabet.substr(2) + alphabet.substring(0, 2);
  const rotated_alphabet_map = {};

  for (let i = 0; i < alphabet.length; i++) {
    rotated_alphabet_map[alphabet[i]] = rotated_alphabet[i];
  }

  var encrypted_string = '';

  for (const c of s) {
    if (rotated_alphabet_map[c]) {
      encrypted_string += rotated_alphabet_map[c];
    } else {
      encrypted_string += c;
    }
  }

  return encrypted_string;
}



