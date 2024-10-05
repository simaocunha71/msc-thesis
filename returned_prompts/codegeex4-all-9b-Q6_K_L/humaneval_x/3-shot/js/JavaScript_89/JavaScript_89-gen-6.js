  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  var encrypted = '';
  for (const c of s) {
    let index = alphabet.indexOf(c);
    if (index == -1) {
      encrypted += c;
    } else {
      let new_index = (index + 2 * 2) % alphabet.length;
      encrypted += alphabet[new_index];
    }
  }
  return encrypted;
}