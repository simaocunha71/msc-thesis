  if (n == 0 || n == 1) {
    return 0;
  } else if (n == 2) {
    return 2;
  } else if (n == 3) {
    return 0;
  } else {
    var a = 0;
    var b = 2;
    var c = 0;
    var d = 0;
    for (let i = 4; i <= n; i++) {
      c = a + b + d;
      if (i % 2 == 0) {
        d = c;
      } else {
        a = c;
      }
    }
    return c;
  }
}



