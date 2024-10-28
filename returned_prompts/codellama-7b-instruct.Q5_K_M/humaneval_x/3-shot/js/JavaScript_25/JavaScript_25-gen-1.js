  var factors = [];
  var i = 2;

  while (i <= Math.sqrt(n)) {
    if (n % i == 0) {
      while (n % i == 0) {
        n /= i;
        factors.push(i);
      }
    }
    i++;
  }

  if (n > 1) {
    factors.push(n);
  }

  return factors;
}



