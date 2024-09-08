  const fib = [0, 1];
  for (let i = 2; i < n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
    while (!isPrime(fib[i])) {
      fib[i] += fib[i - 1];
    }
  }
  return fib[n - 1];
}



