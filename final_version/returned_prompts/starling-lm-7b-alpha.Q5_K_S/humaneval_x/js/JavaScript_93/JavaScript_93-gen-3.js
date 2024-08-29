  let result = "";
  for (const c of message) {
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
      result += String.fromCharCode(c.charCodeAt(0) + 2);
    } else if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
      result += String.fromCharCode(c.charCodeAt(0) + 2);
    } else {
      result += String.fromCharCode(c.charCodeAt(0) - 32);
    }
  }
  return result;
}



