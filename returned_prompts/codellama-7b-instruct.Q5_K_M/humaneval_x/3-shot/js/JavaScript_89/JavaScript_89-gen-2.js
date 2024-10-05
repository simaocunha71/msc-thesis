  var result = '';
  var alphabet = 'abcdefghijklmnopqrstuvwxyz';
  var rotated = alphabet.slice(2) + alphabet.slice(0, 2);
  for (const c of s) {
    var index = alphabet.indexOf(c);
    if (index != -1) {
      result += rotated[index];
    } else {
      result += c;
    }
  }
  return result;
}



