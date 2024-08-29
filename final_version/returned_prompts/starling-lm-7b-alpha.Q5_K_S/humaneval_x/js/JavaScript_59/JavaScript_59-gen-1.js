  while (n % 2 === 0) {
    n /= 2;
  }

  for (let i = 3; i * i <= n; i += 2) {
    while (n % i === 0) {
      n /= i;
    }
  }

  return n;
}



