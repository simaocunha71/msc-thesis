  var factors = [];
  var d = 2;
  while (d * d <= n) {
    while (n % d == 0) {
      factors.push(d);
      n /= d;
    }
    d += 1;
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}