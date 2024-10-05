  if (n == 0) return 0;
  if (n == 1) return 0;
  if (n == 2) return 1;

  var fib = [0, 0, 1];
  for (var i = 3; i <= n; i++) {
    fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
  }
  return fib[n];
}



