  if (n <= 1) {
    return 0;
  }
  if (n == 2) {
    return 2;
  }
  var a = 0, b = 0, c = 2, d = 0;
  for (let i = 3; i <= n; i++) {
    var temp = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = temp;
  }
  return d;
}