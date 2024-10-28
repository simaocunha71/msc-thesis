  var factors = [];
  var i = 2;

  while (n > 1) {
    if (n % i == 0) {
      factors.push(i);
      n = n / i;
    } else {
      i += 1;
    }
  }

  return factors;
}



