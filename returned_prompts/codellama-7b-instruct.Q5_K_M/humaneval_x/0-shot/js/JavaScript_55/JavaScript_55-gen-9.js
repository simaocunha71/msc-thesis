const fib = (n) => {
  if (n < 2) return n;
  const a = fib(n - 1);
  const b = fib(n - 2);
  return a + b;
};
