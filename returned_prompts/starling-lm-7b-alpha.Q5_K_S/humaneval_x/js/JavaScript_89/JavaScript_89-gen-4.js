  let result = '';

  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    let code = c.charCodeAt(0);
    if (code >= 97 && code <= 122) {
      result += String.fromCharCode((code - 97 + 2 * 2 * 2) % 26 + 97);
    } else if (code >= 65 && code <= 90) {
      result += String.fromCharCode((code - 65 + 2 * 2 * 2) % 26 + 65);
    } else {
      result += c;
    }
  }

  return result;
}



