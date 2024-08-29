  if (s0.length != s1.length) {
    return false;
  }
  let s0_chars = {};
  let s1_chars = {};

  for (const char of s0) {
    if (s0_chars[char] == undefined) {
      s0_chars[char] = 0;
    }
    s0_chars[char] += 1;
  }

  for (const char of s1) {
    if (s1_chars[char] == undefined) {
      s1_chars[char] = 0;
    }
    s1_chars[char] += 1;
  }

  for (const key in s0_chars) {
    if (s1_chars[key] == undefined || s0_chars[key] != s1_chars[key]) {
      return false;
    }
  }
  return true;
}



