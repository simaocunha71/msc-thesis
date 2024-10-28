  if (s0.length != s1.length) return false;

  const counts0 = {};
  for (const c of s0) {
    if (counts0[c] == undefined) counts0[c] = 0;
    counts0[c] += 1;
  }

  const counts1 = {};
  for (const c of s1) {
    if (counts1[c] == undefined) counts1[c] = 0;
    counts1[c] += 1;
  }

  for (const c of s0) {
    if (counts0[c] != counts1[c]) return false;
  }

  return true;
}



