  let s0_count = {};
  let s1_count = {};

  for (let c of s0) {
    s0_count[c] = (s0_count[c] || 0) + 1;
  }

  for (let c of s1) {
    s1_count[c] = (s1_count[c] || 0) + 1;
  }

  return Object.keys(s0_count).length == Object.keys(s1_count).length &&
    Object.keys(s0_count).every(key => s0_count[key] == s1_count[key]);
}



