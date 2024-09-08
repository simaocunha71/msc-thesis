  const factors = [];
  let d = 2;
  while (d * d <= n) {
    if (n % d == 0) {
      factors.push(d);
      while (n % d == 0) {
        n /= d;
      }
    }
    d += 1;
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}



