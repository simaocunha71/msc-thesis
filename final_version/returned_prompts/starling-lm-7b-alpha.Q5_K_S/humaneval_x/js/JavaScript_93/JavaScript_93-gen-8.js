  let result = '';
  for (const c of message) {
    if (c == ' ') {
      result += c;
    } else if (c == '.') {
      result += c;
    } else if (c == ',') {
      result += c;
    } else if (c == '?') {
      result += c;
    } else if (c == '!') {
      result += c;
    } else if (c == '"') {
      result += c;
    } else if (c == "'") {
      result += c;
    } else if (c == '@') {
      result += c;
    } else if (c == '#') {
      result += c;
    } else if (c == '$') {
      result += c;
    } else if (c == '%') {
      result += c;
    } else if (c == '^') {
      result += c;
    } else if (c == '&') {
      result += c;
    } else if (c == '*') {
      result += c;
    } else if (c == '(') {
      result += c;
    } else if (c == ')') {
      result += c;
    } else if (c == '{') {
      result += c;
    } else if (c == '}') {
      result += c;
    } else {
      const ascii_val = c.charCodeAt(0);
      if (ascii_val >= 65 && ascii_val <= 90) {
        result += String.fromCharCode((ascii_val - 65 + 1) % 26 + 65);
      } else if (ascii_val >= 97 && ascii_val <= 122) {
        result += String.fromCharCode((ascii_val - 97 + 1) % 26 + 97);
      }
    }
  }

  return result;
}



