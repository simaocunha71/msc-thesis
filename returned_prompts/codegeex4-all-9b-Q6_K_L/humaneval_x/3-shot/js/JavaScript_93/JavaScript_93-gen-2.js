  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  let result = '';
  for (const c of message) {
    if (vowels.includes(c)) {
      result += String.fromCharCode(c.charCodeAt(0) + 2);
    } else if (c == c.toLowerCase()) {
      result += c.toUpperCase();
    } else {
      result += c.toLowerCase();
    }
  }
  return result;
}