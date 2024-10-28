  let s0_map = {};
  let s1_map = {};

  for (const c of s0) {
    if (s0_map[c] == null) {
      s0_map[c] = 1;
    } else {
      s0_map[c] += 1;
    }
  }

  for (const c of s1) {
    if (s1_map[c] == null) {
      s1_map[c] = 1;
    } else {
      s1_map[c] += 1;
    }
  }

  for (const key in s0_map) {
    if (s1_map[key] == null || s0_map[key] != s1_map[key]) {
      return false;
    }
  }

  return true;
}