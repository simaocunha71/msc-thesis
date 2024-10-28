  let encoded = '';
  for (const c of message) {
    if (c.match(/[a-z]/i)) {
      if (c.match(/[aeiou]/i)) {
        encoded += String.fromCharCode((c.charCodeAt(0) + 2) % 26 + 97);
      } else {
        encoded += c.toUpperCase();
      }
    } else {
      encoded += c;
    }
  }
  return encoded;
}