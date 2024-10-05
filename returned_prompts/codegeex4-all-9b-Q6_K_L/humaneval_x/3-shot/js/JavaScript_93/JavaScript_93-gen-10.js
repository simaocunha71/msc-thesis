  var result = "";
  for (let i = 0; i < message.length; i++) {
    var c = message.charAt(i);
    if (c == c.toUpperCase()) {
      if (c == 'A') {
        result += 'C';
      } else if (c == 'E') {
        result += 'G';
      } else if (c == 'I') {
        result += 'K';
      } else if (c == 'O') {
        result += 'Q';
      } else if (c == 'U') {
        result += 'W';
      } else {
        result += c.toLowerCase();
      }
    } else {
      if (c == 'a') {
        result += 'c';
      } else if (c == 'e') {
        result += 'g';
      } else if (c == 'i') {
        result += 'k';
      } else if (c == 'o') {
        result += 'q';
      } else if (c == 'u') {
        result += 'w';
      } else {
        result += c.toUpperCase();
      }
    }
  }
  return result;
}