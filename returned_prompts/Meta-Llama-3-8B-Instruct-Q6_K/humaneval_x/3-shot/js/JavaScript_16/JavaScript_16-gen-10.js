  let char_set = new Set();
  for (let char of string.toLowerCase()) {
    char_set.add(char);
  }
  return char_set.size;
}
