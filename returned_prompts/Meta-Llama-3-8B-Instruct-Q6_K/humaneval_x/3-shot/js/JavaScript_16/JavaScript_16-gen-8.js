  let seen = new Set();
  for (const c of string.toLowerCase()) {
    if (!seen.has(c)) {
      seen.add(c);
    }
  }
  return seen.size;
}



