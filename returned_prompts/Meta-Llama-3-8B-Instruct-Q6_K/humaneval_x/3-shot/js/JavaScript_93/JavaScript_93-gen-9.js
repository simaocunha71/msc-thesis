  let result = '';
  for (let i = 0; i < message.length; i++) {
    const c = message[i];
    if (c >= 'a' && c <= 'z') {
      result += String.fromCharCode(c.charCodeAt(0) + (c === 'a' ? 0 : c === 'e' ? 2 : c === 'i' ? 2 : c === 'o' ? 2 : c === 'u' ? 2 : 0));
    } else if (c >= 'A' && c <= 'Z') {
      result += String.fromCharCode(c.charCodeAt(0) - (c === 'A' ? 0 : c === 'E' ? 2 : c === 'I' ? 2 : c === 'O' ? 2 : c === 'U' ? 2 : 0));
    } else {
      result += c;
    }
  }
  return result;
}