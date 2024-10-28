  let char_set = new Set();
  for (let c of string.toLowerCase()) {
    char_set.add(c);
  }
  return char_set.size;
}