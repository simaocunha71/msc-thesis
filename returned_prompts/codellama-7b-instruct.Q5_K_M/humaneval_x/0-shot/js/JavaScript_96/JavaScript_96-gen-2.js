const countUpTo = (n) => {
  if (n < 2) return [];
  const primes = [2];
  for (let i = 3; i < n; i += 2) {
    let isPrime = true;
    for (let j = 2; j < primes.length; j++) {
      if (i % primes[j] === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) primes.push(i);
  }
  return primes;
};

