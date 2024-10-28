  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 0;
  }
  if (n == 2) {
    return 1;
  }

  var a = 0;
  var b = 0;
  var c = 1;

  for (let i = 3; i <= n; i++) {
    a = b;
    b = c;
    c = a + b + c;
  }

  return c;
}



