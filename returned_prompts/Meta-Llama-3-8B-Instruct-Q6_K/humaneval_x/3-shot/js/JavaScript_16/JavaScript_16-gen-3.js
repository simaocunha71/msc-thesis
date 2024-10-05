  let charSet = new Set();
  for (let char of string.toLowerCase()) {
    if (!char.match(/[a-z]/)) {
      continue;
    }
    charSet.add(char);
  }
  return charSet.size;
}