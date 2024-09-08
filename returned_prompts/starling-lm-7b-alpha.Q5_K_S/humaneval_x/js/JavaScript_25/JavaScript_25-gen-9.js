  const primes = [];
  const table = new Array(n + 1).fill(true);

  table[0] = false;
  table[1] = false;

  for (let i = 2; i <= n; i++) {
    if (table[i]) {
      primes.push(i);
      for (let j = i * i; j <= n; j += i) {
        table[j] = false;
      }
    }
  }

  const result = [];

  while (n > 1) {
    const p = primes.find(prime => n % prime === 0);
    result.push(p);
    while (n % p === 0) {
      n /= p;
    }
  }

  return result;
}



