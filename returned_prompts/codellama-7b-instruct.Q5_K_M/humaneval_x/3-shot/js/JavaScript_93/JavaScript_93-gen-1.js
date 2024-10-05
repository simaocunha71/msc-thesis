  var result = '';
  var vowels = ['a', 'e', 'i', 'o', 'u'];

  for (let i = 0; i < message.length; i++) {
    var c = message[i];
    if (vowels.indexOf(c) != -1) {
      c = String.fromCharCode((vowels.indexOf(c) + 2) % 26 + 97);
    } else {
      c = String.fromCharCode(c.charCodeAt(0) ^ 32);
    }
    result += c;
  }

  return result;
}



