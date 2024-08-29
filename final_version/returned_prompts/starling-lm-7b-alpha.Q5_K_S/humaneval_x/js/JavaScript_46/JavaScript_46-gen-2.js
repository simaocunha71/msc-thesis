  if (n == 0 || n == 1) return 0;
  if (n == 2) return 2;
  if (n == 3) return 0;

  const fib_sequence = [0, 0, 2];

  for (let i = 4; i <= n; i++) {
    fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2] + fib_sequence[i - 3] + fib_sequence[i - 4];
  }

  return fib_sequence[n];
}



