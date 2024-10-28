  let factors = [];
  let i = 2;

  while (i * i <= n) {
    while (n % i == 0) {
      factors.push(i);
      n = n / i;
    }
    i++;
  }

  if (n > 1) {
    factors.push(n);
  }

  return factors;
}