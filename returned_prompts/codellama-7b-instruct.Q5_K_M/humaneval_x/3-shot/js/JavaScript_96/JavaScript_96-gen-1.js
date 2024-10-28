  if (n < 1) {
    return [];
  }

  var primes = [];

  for (let i = 1; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }

  return primes;
}



