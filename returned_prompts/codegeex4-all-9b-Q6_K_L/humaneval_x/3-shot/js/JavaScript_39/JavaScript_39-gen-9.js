  let fib = [0, 1, 1];
  let count = 0;
  for (let i = 3; count < n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
    if (isPrime(fib[i])) {
      count += 1;
    }
  }
  return fib[n];
}



