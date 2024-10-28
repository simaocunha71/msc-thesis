  var factors = [];
  var i = 2;
  while (i * i <= n) {
    if (n % i) {
      i += 1;
    } else {
      n /= i;
      factors.push(i);
    }
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}



