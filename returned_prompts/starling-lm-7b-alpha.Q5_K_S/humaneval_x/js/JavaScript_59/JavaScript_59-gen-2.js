  const isPrime = (n) => {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return n > 1;
  }

  while (n % 2 === 0) {
    n /= 2;
  }

  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    if (isPrime(i)) {
      while (n % i === 0) {
        n /= i;
      }
    }
  }

  return n;
}



