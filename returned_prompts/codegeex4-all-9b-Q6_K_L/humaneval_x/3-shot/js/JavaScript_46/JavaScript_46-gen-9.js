  var fib4 = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    fib4.push(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4]);
  }
  return fib4[n];
}