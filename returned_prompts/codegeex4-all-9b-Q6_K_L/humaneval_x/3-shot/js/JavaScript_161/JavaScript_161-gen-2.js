  var result = '';
  for (var i = 0; i < s.length; i++) {
    var c = s[i];
    if (c >= 'A' && c <= 'Z') {
      result += c.toLowerCase();
    } else if (c >= 'a' && c <= 'z') {
      result += c.toUpperCase();
    } else {
      result += c;
    }
  }
  return result.split('').reverse().join('');
}



