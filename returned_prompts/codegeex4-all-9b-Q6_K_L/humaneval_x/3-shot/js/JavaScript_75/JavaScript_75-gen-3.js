  const isPrime = (n) => {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  };

  const primes = [];
  for (let i = 2; i <= a; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }

  let product = 1;
  for (let i = 0; i < primes.length; i++) {
    product *= primes[i];
    if (product == a) {
      return true;
    }
  }

  return false;
}

