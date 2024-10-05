  var distinctCharacters = new Set();

  for (const c of string) {
    distinctCharacters.add(c.toLowerCase());
  }

  return distinctCharacters.size;
}