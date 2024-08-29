  const char_set = new Set();
  for (const c of string) {
    char_set.add(c.toLowerCase());
  }

  return char_set.size;
}



