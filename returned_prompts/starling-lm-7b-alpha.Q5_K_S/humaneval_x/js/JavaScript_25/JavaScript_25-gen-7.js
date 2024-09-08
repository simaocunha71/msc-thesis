  const primes = [];
  while (n % 2 === 0) {
    primes.push(2);
    n /= 2;
  }
  for (let i = 3; i * i <= n; i += 2) {
    while (n % i === 0) {
      primes.push(i);
      n /= i;
    }
  }
  if (n > 2) {
    primes.push(n);
  }
  return primes;
}



