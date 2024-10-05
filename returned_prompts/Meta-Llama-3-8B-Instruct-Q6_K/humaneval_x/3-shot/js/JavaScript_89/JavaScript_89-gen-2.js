  let result = '';
  for (let i = 0; i < s.length; i++) {
    let c = s.charCodeAt(i);
    if (c >= 65 && c <= 90) {
      c = (c - 65 + 26 * 2) % 26 + 65;
    } else if (c >= 97 && c <= 122) {
      c = (c - 97 + 26 * 2) % 26 + 97;
    }
    result += String.fromCharCode(c);
  }
  return result;
}