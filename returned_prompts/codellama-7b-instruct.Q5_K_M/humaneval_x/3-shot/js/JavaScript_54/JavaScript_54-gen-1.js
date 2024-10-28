  if (s0.length != s1.length) {
    return false;
  }

  var c0 = new Set();
  for (const c of s0) {
    if (c0.has(c)) {
      return false;
    }
    c0.add(c);
  }

  var c1 = new Set();
  for (const c of s1) {
    if (c0.has(c)) {
      return false;
    }
    c1.add(c);
  }

  return c0.size == c1.size;
}



