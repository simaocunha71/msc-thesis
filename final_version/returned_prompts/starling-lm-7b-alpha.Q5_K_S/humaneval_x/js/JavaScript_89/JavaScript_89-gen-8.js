  let result = '';
  for (const c of s) {
    let char_code = c.charCodeAt(0);
    if (char_code >= 97 && char_code <= 122) {
      char_code += 2 * 2;
      result += String.fromCharCode(char_code);
    } else {
      result += c;
    }
  }
  return result;
}



