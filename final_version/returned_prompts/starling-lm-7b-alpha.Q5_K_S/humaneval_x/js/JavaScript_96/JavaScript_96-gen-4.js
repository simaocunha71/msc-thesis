  const sieve = Array.from({ length: n + 1 }, (v, i) => i);
  sieve[0] = false;
  sieve[1] = false;

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (sieve[i]) {
      for (let j = i * i; j <= n; j += i) {
        sieve[j] = false;
      }
    }
  }

  return sieve.slice(0, n).filter(Boolean);
}



