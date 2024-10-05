  if (n < 1) {
    return 0;
  }
  if (n == 1) {
    return 0;
  }
  if (n == 2) {
    return 2;
  }
  let a = 0;
  let b = 0;
  let c = 2;
  let d = 0;
  for (let i = 3; i <= n; i++) {
    let sum = a + b + c + d;
    d = c;
    c = b;
    b = a;
    a = sum;
  }
  return a;
}
