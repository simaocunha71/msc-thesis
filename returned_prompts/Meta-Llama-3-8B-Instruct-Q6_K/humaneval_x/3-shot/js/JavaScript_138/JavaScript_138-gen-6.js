  for (let a = 2; a < n; a += 2) {
    for (let b = 2; b < n; b += 2) {
      for (let c = 2; c < n; c += 2) {
        for (let d = 2; d < n; d += 2) {
          if (a + b + c + d === n) {
            return true;
          }
        }
      }
    }
  }
  return false;
}