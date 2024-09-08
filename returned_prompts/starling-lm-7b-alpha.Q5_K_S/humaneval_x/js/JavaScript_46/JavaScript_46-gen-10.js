  const fib4 = [0, 0, 2, 0];
  while (fib4.length <= n) {
    fib4.push(fib4[fib4.length - 1] + fib4[fib4.length - 2] + fib4[fib4.length - 3] + fib4[fib4.length - 4]);
  }
  return fib4[n];
}



