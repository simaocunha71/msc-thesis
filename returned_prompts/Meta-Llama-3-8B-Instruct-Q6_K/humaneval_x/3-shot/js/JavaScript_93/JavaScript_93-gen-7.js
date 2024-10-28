  let result = '';
  for (let c of message) {
    if (c.match(/[a-z]/)) {
      if (c.match(/[aeiou]/i)) {
        result += String.fromCharCode((c.charCodeAt(0) + 2) % 26 + 97);
      } else {
        result += c.toUpperCase();
      }
    } else if (c.match(/[A-Z]/)) {
      if (c.match(/[AEIOU]/i)) {
        result += String.fromCharCode((c.charCodeAt(0) + 2) % 26 + 65);
      } else {
        result += c.toLowerCase();
      }
    } else {
      result += c;
    }
  }
  return result;
}