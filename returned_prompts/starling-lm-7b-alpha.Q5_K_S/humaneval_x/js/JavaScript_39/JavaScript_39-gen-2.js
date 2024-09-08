  let fib = [0, 1];
  let primes = [2];
  let candidate;

  while (fib.length < n) {
    candidate = fib[fib.length - 1] + fib[fib.length - 2];
    if (isPrime(candidate)) {
      fib.push(candidate);
      primes.push(candidate);
    }
  }

  return fib[n - 1];
}



