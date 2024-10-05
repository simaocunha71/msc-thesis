  var count = 0;
  var seen = new Set();

  for (const c of string) {
    if (!seen.has(c)) {
      count += 1;
      seen.add(c);
    }
  }

  return count;
}



