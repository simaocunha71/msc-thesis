  let maxFactor = 1;

  for (let i = 2; i * i <= n; i++) {
    while (n % i === 0) {
      maxFactor = i;
      n /= i;
    }
  }

  if (n > 1) {
    maxFactor = n;
  }

  return maxFactor;
}