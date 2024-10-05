  while (n % 2 == 0) {
    n = n / 2;
  }

  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    while (n % i == 0) {
      n = n / i;
    }
  }

  return n;
}



