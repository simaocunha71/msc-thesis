  const fib4_series = [0, 0, 2];
  while (fib4_series.length <= n) {
    fib4_series.push(fib4_series[fib4_series.length - 1] + fib4_series[fib4_series.length - 2] + fib4_series[fib4_series.length - 3] + fib4_series[fib4_series.length - 4]);
  }
  return fib4_series[n];
}



