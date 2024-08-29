  let distinct = new Set();

  for (const c of string) {
    distinct.add(c.toLowerCase());
  }

  return distinct.size;
}



