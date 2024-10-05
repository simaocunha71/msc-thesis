  if (n == 0 || n == 1) {
    return 0;
  } else if (n == 2) {
    return 2;
  } else if (n == 3) {
    return 0;
  } else {
    let a = 0;
    let b = 0;
    let c = 2;
    let d = 0;
    let result = 0;
    for (let i = 4; i <= n; i++) {
      result = a + b + c + d;
      a = b;
      b = c;
      c = d;
      d = result;
    }
    return result;
  }
}