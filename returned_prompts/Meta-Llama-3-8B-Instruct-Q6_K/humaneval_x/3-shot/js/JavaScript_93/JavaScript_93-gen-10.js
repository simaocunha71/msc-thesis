  let result = '';
  for (let c of message) {
    if (c === c.toUpperCase()) {
      result += c.toLowerCase();
    } else {
      result += c.toUpperCase();
    }
    if (c.match(/[aeiouAEIOU]/)) {
      let index = 'abcdefghijklmnopqrstuvwxyz'.indexOf(c.toLowerCase());
      result += 'abcdefghijklmnopqrstuvwxyz'[index + 2];
    } else {
      result += c;
    }
  }
  return result;
}