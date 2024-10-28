  let map = {};
  for (let i = 0; i < l.length; i++) {
    if (map[-l[i]]) {
      return true;
    }
    map[l[i]] = true;
  }
  return false;
}



