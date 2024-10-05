  const set = new Set(l);

B:
  for (let i = 0; i < set.size; i++) {
    for (let j = i + 1; j < set.size; j++) {
      for (let k = j + 1; k < set.size; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
}


