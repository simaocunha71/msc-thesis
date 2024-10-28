  const fib = (n) => {
    if (n <= 1) {
      return n;
    }
    return fib(n - 1) + fib(n - 2);
  };

  const isPrime = (n) => {
    if (n <= 1) {
      return false;
    }
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  };

  return fib(n);

}
