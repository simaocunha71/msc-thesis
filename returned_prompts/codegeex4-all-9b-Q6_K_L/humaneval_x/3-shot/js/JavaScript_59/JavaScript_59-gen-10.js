  var factors = [];

  for (var i = 2; i <= n; i++) {
    while (n % i == 0) {
      factors.push(i);
      n = n / i;
    }
  }

  return factors[factors.length - 1];
}