  const primes = [];
  const isPrime = (num) => {
    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return num > 1;
  };

  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }

  return primes;
}



