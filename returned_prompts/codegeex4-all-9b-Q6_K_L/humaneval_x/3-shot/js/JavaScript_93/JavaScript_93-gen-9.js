  var vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  var result = '';
  for (const c of message) {
    if (vowels.includes(c)) {
      result += String.fromCharCode(c.charCodeAt(0) + 2);
    } else if (c == c.toUpperCase()) {
      result += c.toLowerCase();
    } else {
      result += c.toUpperCase();
    }
  }
  return result;
}