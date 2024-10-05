  if (n <= 2) return 0;
  let a = 0;
  let b = 0;
  let c = 1;
  for (let i = 3; i <= n; i++) {
    a = b;
    b = c;
    c = a + b + c;
  }
  return c;
}



