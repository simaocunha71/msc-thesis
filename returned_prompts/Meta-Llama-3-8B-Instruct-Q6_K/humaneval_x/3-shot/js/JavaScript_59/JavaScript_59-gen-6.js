  for (let i = Math.floor(Math.sqrt(n)); i > 1; i--) {
    while (n % i == 0) {
      n = n / i;
    }
  }
  return n;
}