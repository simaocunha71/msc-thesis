  var result = "";
  for (let c of message) {
    if (c == c.toUpperCase()) {
      result += c.toLowerCase();
    } else {
      result += c.toUpperCase();
    }

    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
      result += String.fromCharCode(c.charCodeAt(0) + 2);
    } else if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
      result += String.fromCharCode(c.charCodeAt(0) + 2);
    } else {
      result += c;
    }
  }
  return result;
}