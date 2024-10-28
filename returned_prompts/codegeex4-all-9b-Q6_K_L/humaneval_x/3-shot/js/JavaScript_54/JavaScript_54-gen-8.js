  let map = {};
  for (const c of s0) {
    map[c] = true;
  }

  for (const c of s1) {
    if (map[c] == undefined) {
      return false;
    }
  }

  return true;
}



