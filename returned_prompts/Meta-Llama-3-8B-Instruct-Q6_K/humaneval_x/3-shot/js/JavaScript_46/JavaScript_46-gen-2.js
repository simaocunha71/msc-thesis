  if (n <= 3) {
    return [0, 0, 2, 0][n - 1];
  }
  let a = 0, b = 0, c = 2, d = 0, e = 0;
  for (let i = 4; i <= n; i++) {
    e = a + b + c + d;
    d = c;
    c = b;
    b = a;
    a = e;
  }
  return e;
}