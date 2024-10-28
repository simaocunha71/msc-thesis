  let fib = [0,0,2];
  for (let i = 3; i <= n; i++) {
    fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
  }
  return fib[n];
}



