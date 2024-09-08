  const isPrime = (num) => {
    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  };

  while (n % 2 === 0) {
    n /= 2;
  }

  for (let i = 3; i * i <= n; i += 2) {
    if (isPrime(i) && n % i === 0) {
      n /= i;
    }
  }

  return n;
}



