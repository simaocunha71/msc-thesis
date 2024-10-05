  if (n <= 3) {
    return [0, 0, 2, 0][n - 1];
  }
  let fib4_array = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    fib4_array.push((fib4_array[i - 1] + fib4_array[i - 2] + fib4_array[i - 3] + fib4_array[i - 4]) % 10);
  }
  return fib4_array[n - 1];
}