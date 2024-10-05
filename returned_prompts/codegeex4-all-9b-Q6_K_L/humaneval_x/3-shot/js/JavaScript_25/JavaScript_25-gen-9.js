  var factors = [];
  var i = 2;

  while (i <= n) {
    if (n % i == 0) {
      factors.push(i);
      n /= i;
    } else {
      i += 1;
    }
  }

  return factors;
}



