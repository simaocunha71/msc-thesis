  const s0_chars = new Set(s0.split(''));
  const s1_chars = new Set(s1.split(''));
  if (s0_chars.size != s1_chars.size) {
    return false;
  }
  for (const char of s0_chars) {
    if (!s1_chars.has(char)) {
      return false;
    }
  }
  return true;
}



