  for (let i = 2; i <= n; i += 2) {
    for (let j = 2; j <= n; j += 2) {
      for (let k = 2; k <= n; k += 2) {
        for (let l = 2; l <= n; l += 2) {
          if (i + j + k + l == n) {
            return true;
          }
        }
      }
    }
  }
  return false;
}



