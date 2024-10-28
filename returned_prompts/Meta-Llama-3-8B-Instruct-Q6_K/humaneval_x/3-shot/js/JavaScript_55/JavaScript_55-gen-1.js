  if (n <= 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    let a = 1, b = 1;
    for (let i = 2; i < n; i++) {
      let c = a + b;
      a = b;
      b = c;
    }
    return b;
  }
}