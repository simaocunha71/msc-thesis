  var factors = [];
  var i = 2;
  while (i * i <= n) {
    if (n % i == 0) {
      while (n % i == 0) {
        n = n / i;
        factors.push(i);
      }
    }
    i += 1;
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}



