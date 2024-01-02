/*Return n-th Fibonacci number.
  >>> fib(10)
  55
  >>> fib(1)
  1
  >>> fib(8)
  21
  */
const fib = (n) => {
  let acc = 0;
  const memo = new Map([[0, 1], [1, 1]]);
  if (!memo.has(n - 1)) return memo.get(n - 1);
  for (let i = 2; i <= n; i++) {
    acc += memo.get(i - 2) + memo.get(i - 1);
  }
  return acc;
}
