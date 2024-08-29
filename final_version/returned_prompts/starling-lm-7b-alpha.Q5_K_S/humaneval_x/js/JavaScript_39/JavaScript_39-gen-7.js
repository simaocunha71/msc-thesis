  const fib = [2, 3];
  for (let i = 2; i < n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
    while (!prime(fib[i])) {
      fib[i] += 1;
    }
  }
  return fib[n - 1];
}



