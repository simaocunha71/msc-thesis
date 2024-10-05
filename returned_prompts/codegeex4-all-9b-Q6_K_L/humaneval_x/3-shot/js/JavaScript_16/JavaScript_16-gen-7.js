  var result = new Set();
  for (const c of string) {
    result.add(c.toLowerCase());
  }
  return result.size;
}