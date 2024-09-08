  const fibfib_cache = [0, 0, 1];
  if (n < 3) return fibfib_cache[n];

  for (let i = 3; i <= n; i++) {
    fibfib_cache[i] = fibfib_cache[i - 1] + fibfib_cache[i - 2] + fibfib_cache[i - 3];
  }
  return fibfib_cache[n];
}



