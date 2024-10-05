  if (s0.length !== s1.length) {
    return false;
  }
  var hash = {};
  for (let i = 0; i < s0.length; i++) {
    if (hash[s0[i]]) {
      hash[s0[i]]++;
    } else {
      hash[s0[i]] = 1;
    }
  }
  for (let i = 0; i < s1.length; i++) {
    if (hash[s1[i]]) {
      hash[s1[i]]--;
      if (hash[s1[i]] < 0) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
}