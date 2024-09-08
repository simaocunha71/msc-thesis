  let distinct = new Set();
  for (const c of string) {
    if (c != ' ') {
      distinct.add(c.toLowerCase());
    }
  }
  return distinct.size;
}



