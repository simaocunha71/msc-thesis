  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let result = '';
  for (const c of message) {
    if (c == c.toUpperCase()) {
      if (vowels.includes(c.toLowerCase())) {
        result += String.fromCharCode(c.charCodeAt(0) + 2);
      } else {
        result += c.toLowerCase();
      }
    } else {
      if (vowels.includes(c)) {
        result += String.fromCharCode(c.charCodeAt(0) - 32 + 2);
      } else {
        result += c.toUpperCase();
      }
    }
  }
  return result;
}

