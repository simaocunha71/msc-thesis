const fib4 = (n) => {
  let a = 0, b = 0, c = 2;
  while (n > 0) {
    if (n & 1) {
      c = a + b + c;
    }
    a = b;
    b = c;
    n >>= 1;
  }
  return c;
}
