  let result = '';
  for (let c of message) {
    if (c.match(/[a-z]/i)) {
      if (c.match(/[aeiou]/i)) {
        c = String.fromCharCode((c.charCodeAt(0) % 26) + 2);
      } else {
        c = c.toUpperCase();
      }
    } else {
      c = c.toLowerCase();
    }
    result += c;
  }
  return result;
} 