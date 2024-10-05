  let result = '';
  for (const c of s) {
    let code = c.charCodeAt(0);
    if (code >= 97 && code <= 122) {
      result += String.fromCharCode((code - 97 + 2 * 2) % 26 + 97);
    } else {
      result += c;
    }
  }
  return result;
}



