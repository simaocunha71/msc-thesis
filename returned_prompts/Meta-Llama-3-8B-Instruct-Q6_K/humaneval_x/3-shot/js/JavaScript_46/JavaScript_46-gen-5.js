  if (n < 4) {
    if (n === 0 || n === 1) {
      return 0;
    } else {
      return 2;
    }
  }

  let a = 0, b = 0, c = 2, d = 0;
  for (let i = 4; i <= n; i++) {
    let temp = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = temp;
  }
  return d;
}