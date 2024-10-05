  var result = '';
  var alphabet = 'abcdefghijklmnopqrstuvwxyz';
  for (const c of s) {
    if (alphabet.indexOf(c) != -1) {
      result += alphabet[(alphabet.indexOf(c) + 2 * 2) % 26];
    } else {
      result += c;
    }
  }
  return result;
}



