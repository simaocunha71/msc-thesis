  let a = 0;
  let b = 1;
  let c;

  if (n <= 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }

  for (let i = 2; i <= n; i++) {
    c = a + b;
    a = b;
    b = c;
  }

  return c;
}

