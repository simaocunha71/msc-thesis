  var s0_set = new Set(s0);
  for (var c of s1) {
    if (!s0_set.has(c)) {
      return false;
    }
  }

  return true;
}



