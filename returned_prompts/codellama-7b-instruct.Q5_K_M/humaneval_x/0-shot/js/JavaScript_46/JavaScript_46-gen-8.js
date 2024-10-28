const fib4 = (n) => {
  let a = 0, b = 0, c = 2, d = 0;
  while (n > 0) {
    d = c;
    c = b;
    b = a;
    a = d + c + b;
    n--;
  }
  return a;
}
