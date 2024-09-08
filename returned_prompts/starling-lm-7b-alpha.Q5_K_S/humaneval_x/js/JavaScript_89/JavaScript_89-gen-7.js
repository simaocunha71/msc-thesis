  let result = "";
  let shift = 2 * 2;
  for (const c of s) {
    let char_code = c.charCodeAt(0);
    if (char_code >= 97 && char_code <= 122) {
      char_code += shift;
      result += String.fromCharCode(char_code);
    } else if (char_code >= 65 && char_code <= 90) {
      char_code += shift;
      result += String.fromCharCode(char_code);
    } else {
      result += c;
    }
  }
  return result;
}



