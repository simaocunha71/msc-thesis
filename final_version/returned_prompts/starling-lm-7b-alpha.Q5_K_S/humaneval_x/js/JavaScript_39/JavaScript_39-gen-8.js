  let fib = [0, 1];
  for (let i = 2; i <= n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
    while (!prime(fib[i])) {
      fib[i]++;
    }
  }

  return fib[n];
}



