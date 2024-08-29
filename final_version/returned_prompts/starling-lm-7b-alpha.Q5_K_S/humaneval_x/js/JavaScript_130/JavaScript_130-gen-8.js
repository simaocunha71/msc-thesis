  const fib = [3];
  for (let i = 0; i <= n; i++) {
    if (i % 2 === 0) {
      fib.push(1 + i / 2);
    } else {
      const last3 = fib[i - 1] + fib[i - 2] + fib[i + 1];
      fib.push(last3);
    }
  }
  return fib;
}



