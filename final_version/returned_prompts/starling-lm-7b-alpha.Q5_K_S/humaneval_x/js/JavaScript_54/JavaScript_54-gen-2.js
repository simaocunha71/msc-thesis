  let s0_char_count = {};
  let s1_char_count = {};

  for (const c of s0) {
    s0_char_count[c] = (s0_char_count[c] || 0) + 1;
  }

  for (const c of s1) {
    s1_char_count[c] = (s1_char_count[c] || 0) + 1;
  }

  return JSON.stringify(s0_char_count) === JSON.stringify(s1_char_count);
}



