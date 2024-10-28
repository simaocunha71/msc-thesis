  var result = '';
  var vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

  for (const c of message) {
    if (vowels.includes(c)) {
      if (c == 'a' || c == 'A') {
        result += 'c';
      } else if (c == 'e' || c == 'E') {
        result += 'g';
      } else if (c == 'i' || c == 'I') {
        result += 'k';
      } else if (c == 'o' || c == 'O') {
        result += 'q';
      } else if (c == 'u' || c == 'U') {
        result += 'w';
      }
    } else {
      if (c == c.toLowerCase()) {
        result += c.toUpperCase();
      } else {
        result += c.toLowerCase();
      }
    }
  }

  return result;
}