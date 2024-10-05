  if (n == 0 || n == 1) {
    return 0;
  }
  if (n == 2) {
    return 2;
  }
  let a = 0;
  let b = 0;
  let c = 0;
  let d = 2;
  for (let i = 3; i <= n; i++) {
    a = b;
    b = c;
    c = d;
    d = a + b + c + d;
  }
  return d;
}