  const fib = [1, 1];
  for (let i = 2; i < n; i++) {
    const newFib = fib[i - 1] + fib[i - 2];
    fib.push(newFib);
  }

  const fibPrime = fib.filter((f) => isPrime(f));

  return fibPrime[n - 1];
};
