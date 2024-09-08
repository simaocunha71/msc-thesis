  const primes = [];
  const factors = [];

  for (let i = 2; i <= n; i++) {
    if (primes.length === 0) {
      primes.push(i);
    } else {
      let j = 0;
      while (i % primes[j] !== 0) {
        j += 1;
      }
      factors.push(primes[j]);
      if (primes[j] === i) {
        primes.push(i);
      } else {
        primes[j] *= i;
      }
    }
  }

  return factors;
}



