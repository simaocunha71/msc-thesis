  let charSet = new Set();
  for (const c of string.toLowerCase()) {
    charSet.add(c);
  }
  return charSet.size;
}