  if (n % 2 == 1 || n < 8) {
    return false;
  }
  for (let a = 2; a <= n / 4; a += 2) {
    for (let b = 2; b <= (n - a) / 3; b += 2) {
      for (let c = 2; c <= (n - a - b) / 2; c += 2) {
        let d = n - a - b - c;
        if (d % 2 == 0) {
          return true;
        }
      }
    }
  }
  return false;
}

