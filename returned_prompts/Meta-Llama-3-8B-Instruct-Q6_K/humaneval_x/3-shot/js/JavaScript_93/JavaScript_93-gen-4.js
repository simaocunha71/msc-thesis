  let result = '';
  for (const char of message) {
    if (char.match(/[a-z]/i)) {
      const c = char.toLowerCase();
      if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u') {
        result += String.fromCharCode((c.charCodeAt(0) + 2) % 26 + 97);
      } else {
        result += c.toUpperCase();
      }
    } else {
      result += char;
    }
  }
  return result;
}