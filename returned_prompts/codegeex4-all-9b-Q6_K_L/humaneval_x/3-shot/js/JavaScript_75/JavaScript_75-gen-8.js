  var factors = [];
  var n = a;
  for (var i = 2; i < Math.sqrt(n) + 1; i++) {
    while (n % i == 0) {
      factors.push(i);
      n = n / i;
    }
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors.length == 3 && factors.every((x) => (x == 2 || x == 3 || x == 5 || x == 7));
}