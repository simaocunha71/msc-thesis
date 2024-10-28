  for (let i = 0; i < l.length; i++) {
    for (let j = 0; j < l.length; j++) {
      if (i != j) {
        if (l[i] + l[j] == 0) {
          return true;
        }
      }
    }
  }
  return false;
}