const sameChars = (s0, s1) => {
  s0 = s0.split('');
  s1 = s1.split('');
  if (s0.length !== s1.length) {
    return false;
  }
  for (let i = 0; i < s0.length; i++) {
    if (s0[i] !== s1[i]) {
      return false;
    }
  }
  return true;
}

