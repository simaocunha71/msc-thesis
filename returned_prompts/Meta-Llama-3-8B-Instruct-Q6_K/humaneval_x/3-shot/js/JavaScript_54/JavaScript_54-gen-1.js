  if (s0.length !== s1.length) {
    return false;
  }
  let s0_count = {};
  for (let c of s0) {
    if (!s0_count[c]) {
      s0_count[c] = 0;
    }
    s0_count[c]++;
  }
  for (let c of s1) {
    if (!s0_count[c]) {
      return false;
    }
    s0_count[c]--;
  }
  for (let count in s0_count) {
    if (s0_count[count] !== 0) {
      return false;
    }
  }
  return true;
}