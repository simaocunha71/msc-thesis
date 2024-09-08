  const set = new Set(l);
  for (const num of l) {
    const target = -num;
    if (set.has(target)) {
      return true;
    }
    for (const other of l) {
      if (num !== other && set.has(target - other)) {
        return true;
      }
    }
  }
  return false;
}



