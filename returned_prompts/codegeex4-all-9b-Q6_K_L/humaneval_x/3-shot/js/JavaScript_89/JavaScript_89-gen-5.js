  var result = '';

  for (var i = 0; i < s.length; i++) {
    var c = s[i];
    var ascii = c.charCodeAt(0);

    if (ascii >= 65 && ascii <= 90) {
      result += String.fromCharCode((ascii + 4 - 65) % 26 + 65);
    } else if (ascii >= 97 && ascii <= 122) {
      result += String.fromCharCode((ascii + 4 - 97) % 26 + 97);
    } else {
      result += c;
    }
  }

  return result;
}



