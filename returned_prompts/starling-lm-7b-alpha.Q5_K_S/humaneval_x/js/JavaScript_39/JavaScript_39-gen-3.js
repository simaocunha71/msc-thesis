  const fib = [0, 1];
  for (let i = 2; i < 100000; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
    if (fib[i] % 2 != 0 && fib[i] != 1) {
      for (let j = 2; j < fib[i]; j++) {
        if (fib[i] % j == 0) {
          break;
        }
        if (j > fib[i] - 1) {
          return fib[i];
        }
      }
    }
  }
}



