  var alphabet = "abcdefghijklmnopqrstuvwxyz";
  var shifted_alphabet = alphabet.slice(2*2) + alphabet.slice(0, 2*2);
  var result = "";
  for (const c of s) {
    var index = alphabet.indexOf(c);
    if (index != -1) {
      result += shifted_alphabet[index];
    } else {
      result += c;
    }
  }
  return result;
}