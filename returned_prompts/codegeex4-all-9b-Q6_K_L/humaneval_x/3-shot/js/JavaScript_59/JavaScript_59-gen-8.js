  let factors = [];
  let i = 2;
  while (i * i <= n) {
    if (n % i) {
      i += 1;
    } else {
      n /= i;
      factors.push(i);
    }
  }
  return factors[factors.length - 1];
}