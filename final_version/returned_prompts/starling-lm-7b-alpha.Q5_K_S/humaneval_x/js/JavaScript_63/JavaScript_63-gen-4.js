  if (n == 0 || n == 1 || n == 2) {
    return 0;
  }

  let fib_cache = [0, 0, 1];
  for (let i = 3; i <= n; i++) {
    fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2] + fib_cache[i - 3];
  }

  return fib_cache[n];
}



