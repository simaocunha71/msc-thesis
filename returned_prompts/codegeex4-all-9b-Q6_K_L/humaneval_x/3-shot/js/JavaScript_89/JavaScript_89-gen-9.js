  var alphabet = 'abcdefghijklmnopqrstuvwxyz';
  var result = '';

  for (let i = 0; i < s.length; i++) {
    var c = s[i];
    if (c == ' ') {
      result += ' ';
    } else {
      var index = alphabet.indexOf(c);
      var new_index = (index + 4) % 26;
      result += alphabet[new_index];
    }
  }

  return result;
}



