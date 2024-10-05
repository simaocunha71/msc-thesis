  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 0;
  }
  if (n == 2) {
    return 2;
  }
  if (n == 3) {
    return 0;
  }

  var fib = [0, 0, 2, 0];
  for (var i = 4; i <= n; i++) {
    fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
  }
  return fib[n];
}