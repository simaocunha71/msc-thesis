  var factors = [];
  var current = 2;

  while (current <= n) {
    if (n % current == 0) {
      factors.push(current);
      n /= current;
    } else {
      current += 1;
    }
  }
  return factors;
}