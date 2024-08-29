  if (s.length < 3) {
    return false;
  }

  const charSet = new Set();
  for (let i = 0; i < 3; i++) {
    charSet.add(s[i]);
  }

  for (let i = 3; i < s.length; i++) {
    if (charSet.has(s[i])) {
      return false;
    } else {
      charSet.add(s[i]);
    }
  }

  return true;
}



