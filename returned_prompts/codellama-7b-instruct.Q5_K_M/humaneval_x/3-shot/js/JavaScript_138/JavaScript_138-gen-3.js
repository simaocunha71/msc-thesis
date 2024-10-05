  for (let i = 0; i < n; i += 2) {
    for (let j = i + 2; j < n; j += 2) {
      for (let k = j + 2; k < n; k += 2) {
        if (i + j + k == n) {
          return true;
        }
      }
    }
  }
  return false;
}



