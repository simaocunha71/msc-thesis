  if (s.length < 3) {
    return false;
  }

  let seen = new Set();
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (seen.has(char)) {
      return false;
    }
    seen.add(s[i]);

    if (i + 2 >= s.length) {
      continue;
    }

    if (
      seen.has(s[i + 1]) ||
      seen.has(s[i + 2]) ||
      s[i + 1] === char ||
      s[i + 2] === char
    ) {
      return false;
    }
    seen.add(s[i + 1]);
    seen.add(s[i + 2]);
  }
  return true;
}



