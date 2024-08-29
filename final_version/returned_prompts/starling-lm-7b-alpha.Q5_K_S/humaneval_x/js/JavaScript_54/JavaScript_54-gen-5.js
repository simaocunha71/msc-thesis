  const chars_s0 = [];
  const chars_s1 = [];

  for (const c of s0) {
    if (chars_s0.indexOf(c) === -1) {
      chars_s0.push(c);
    }
  }

  for (const c of s1) {
    if (chars_s1.indexOf(c) === -1) {
      chars_s1.push(c);
    }
  }

  return (chars_s0.length === chars_s1.length);
}



