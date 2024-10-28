  const chars = new Set();
  for (const char of s0) {
    chars.add(char);
  }
  for (const char of s1) {
    if (chars.has(char)) {
      return true;
    }
  }
  return false;
}

