  var factors = [];
  while (n > 1) {
    for (var i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) {
        factors.push(i);
        n /= i;
        break;
      }
    }
  }
  return factors;
}



