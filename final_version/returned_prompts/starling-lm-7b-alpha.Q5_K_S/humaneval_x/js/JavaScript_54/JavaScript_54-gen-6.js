  if (s0.length != s1.length) {
    return false;
  }

  var s0_chars = {};
  var s1_chars = {};

  for (const c of s0) {
    if (!s0_chars[c]) {
      s0_chars[c] = 0;
    }
    s0_chars[c] += 1;
  }

  for (const c of s1) {
    if (!s1_chars[c]) {
      s1_chars[c] = 0;
    }
    s1_chars[c] += 1;
  }

  for (const c in s0_chars) {
    if (s0_chars[c] != s1_chars[c]) {
      return false;
    }
  }

  return true;
}



