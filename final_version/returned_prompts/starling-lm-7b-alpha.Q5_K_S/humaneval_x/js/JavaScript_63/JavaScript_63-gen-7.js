  if (n == 0 || n == 1) return 0;
  if (n == 2) return 1;
  if (n > 2) {
    const a = 0;
    const b = 1;
    let c = 1;
    for (let i = 3; i <= n; i++) {
      c = a + b + c;
      a = b;
      b = c;
    }
    return c;
  }
}



