  const n = l.length;
  const lookup = {};
  for (let i = 0; i < n; i++) {
    const v = l[i];
    if (lookup.hasOwnProperty(v)) {
      return true;
    }
    lookup[v] = true;
  }
  return false;
}



