  let result = "";
  let shift = 2;

  for (const c of s) {
    let char_code = c.charCodeAt(0);
    if (char_code >= 97 && char_code <= 122) {
      result += String.fromCharCode((char_code - 97 + shift) % 26 + 97);
    } else if (char_code >= 65 && char_code <= 90) {
      result += String.fromCharCode((char_code - 65 + shift) % 26 + 65);
    } else {
      result += c;
    }
  }

  return result;
}



