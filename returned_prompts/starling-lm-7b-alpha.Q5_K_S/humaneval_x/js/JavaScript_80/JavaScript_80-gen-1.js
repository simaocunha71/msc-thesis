  if (s.length < 3) {
    return false;
  }

  const chars = Array.from(s);
  let i = 0;

  while (i + 2 < chars.length) {
    const c1 = chars[i];
    const c2 = chars[i + 1];
    const c3 = chars[i + 2];

    if (c1 === c2 || c2 === c3 || c1 === c3) {
      return false;
    }
    i += 1;
  }

  return true;
}



