  var result = 0;
  var set = new Set();

  for (const c of string) {
    let lower = c.toLowerCase();
    if (!set.has(lower)) {
      set.add(lower);
      result += 1;
    }
  }

  return result;
}



