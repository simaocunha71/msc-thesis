  const words = txt.split(/\s+/);
  if (words.length > 1) {
    return words;
  }
  words = txt.split(',');
  if (words.length > 1) {
    return words;
  }
  let count = 0;
  for (const c of txt) {
    if (c == c.toLowerCase()) {
      count += (ord(c) % 2);
    }
  }
  return count;
}



