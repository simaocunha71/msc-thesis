  for (let a = 0; a < n; a += 2) {
    for (let b = a + 2; b < n; b += 2) {
      for (let c = b + 2; c < n; c += 2) {
        for (let d = c + 2; d < n; d += 2) {
          if (a + b + c + d === n) {
            return true;
          }
        }
      }
    }
  }
  return false;
}



