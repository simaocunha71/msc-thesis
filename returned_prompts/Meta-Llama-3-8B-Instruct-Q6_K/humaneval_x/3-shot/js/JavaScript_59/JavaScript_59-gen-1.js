  for (let i = 2; i <= Math.sqrt(n); i++) {
    while (n % i === 0) {
      n = n / i;
    }
  }
  return n;
}