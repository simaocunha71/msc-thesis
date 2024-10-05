  if (s.length < 3) {
    return false;
  }

  const set = new Set();
  for (let i = 0; i < s.length - 1; i++) {
    set.add(s[i] + s[i + 1]);
  }
  return set.size == s.length - 1;
}



