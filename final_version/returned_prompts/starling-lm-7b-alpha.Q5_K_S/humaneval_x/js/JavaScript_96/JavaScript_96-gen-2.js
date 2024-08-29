  let primes = [];
  let i = 2;
  while (primes.length < n) {
    let is_prime = true;
    for (const p of primes) {
      if (i % p == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime) {
      primes.push(i);
    }
    i += 1;
  }
  return primes;
}



