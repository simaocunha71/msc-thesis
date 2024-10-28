  if (s0.length != s1.length) {
    return false;
  }

  let hash0 = {};
  let hash1 = {};

  for (let i = 0; i < s0.length; i++) {
    hash0[s0[i]] = hash0[s0[i]] ? hash0[s0[i]] + 1 : 1;
    hash1[s1[i]] = hash1[s1[i]] ? hash1[s1[i]] + 1 : 1;
  }

  for (const c in hash0) {
    if (hash0[c] != hash1[c]) {
      return false;
    }
  }

  return true;
}

