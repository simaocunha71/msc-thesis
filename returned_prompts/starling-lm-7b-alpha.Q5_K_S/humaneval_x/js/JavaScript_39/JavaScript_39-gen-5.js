  const fibonacci = (n) => {
    if (n <= 2) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
  };

  const isPrime = (n) => {
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (let i = 5; i * i <= n; i += 6) {
      if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
  };

  while (true) {
    if (isPrime(fibonacci(n))) {
      return fibonacci(n);
    } else {
      n += 1;
    }
  }
};



