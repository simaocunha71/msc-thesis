  let result = '';
  for (let c of s.toLowerCase()) {
    if (c >= 'a' && c <= 'z') {
      let newCode = (c.charCodeAt(0) - 'a'.charCodeAt(0) + 2 * 2) % 26 + 'a'.charCodeAt(0);
      result += String.fromCharCode(newCode);
    } else {
      result += c;
    }
  }
  return result;
}