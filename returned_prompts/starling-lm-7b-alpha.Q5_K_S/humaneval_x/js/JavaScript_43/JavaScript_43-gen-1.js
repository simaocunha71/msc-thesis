  const set = new Set(l);
  for (let i = 0; i < l.length; i++) {
    const target = -1 * l[i];
    if (set.has(target)) {
      if (l[i] !== target) {
        return true;
      }
    } else {
      set.add(l[i]);
    }
  }
  return false;
}



