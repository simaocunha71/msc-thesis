  var factors = [];
  var factor = 2;

  while (n > 1) {
    while (n % factor != 0) {
      factor += 1;
    }
    factors.push(factor);
    n /= factor;
  }

  return factors;
}



