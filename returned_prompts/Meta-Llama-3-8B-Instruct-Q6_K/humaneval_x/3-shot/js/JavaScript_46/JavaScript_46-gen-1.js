  let fib4_table = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    let sum = fib4_table[i-1] + fib4_table[i-2] + fib4_table[i-3] + fib4_table[i-4];
    fib4_table.push(sum % 10);
  }
  return fib4_table[n];
}

