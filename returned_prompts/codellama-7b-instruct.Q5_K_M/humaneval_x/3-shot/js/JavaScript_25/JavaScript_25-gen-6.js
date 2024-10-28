  let factors = [];
  while (n > 1) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) {
        factors.push(i);
        n = n / i;
        break;
      }
    }
  }
  return factors;
}



