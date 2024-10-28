  var factors = [];

  while (n % 2 == 0) {
    factors.push(2);
    n = n / 2;
  }

  for (var i = 3; i <= Math.sqrt(n); i += 2) {
    while (n % i == 0) {
      factors.push(i);
      n = n / i;
    }
  }

  if (n > 1) {
    factors.push(n);
  }

  return factors;
}



