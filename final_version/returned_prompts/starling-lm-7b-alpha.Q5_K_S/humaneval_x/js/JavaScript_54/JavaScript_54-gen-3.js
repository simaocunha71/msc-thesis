  let s0_chars = s0.split('');
  let s1_chars = s1.split('');

  if (s0_chars.length != s1_chars.length) {
    return false;
  }

  for (let i = 0; i < s0_chars.length; i++) {
    if (s0_chars[i] != s1_chars[i]) {
      return false;
    }
  }

  return true;
}



