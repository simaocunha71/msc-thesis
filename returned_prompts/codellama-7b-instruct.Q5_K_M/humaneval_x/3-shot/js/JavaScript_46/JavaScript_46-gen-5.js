  var a = 0, b = 1, c = 2, d = 3;
  for (var i = 0; i < n - 3; i++) {
    a = b;
    b = c;
    c = d;
    d = a + b + c + d;
  }
  return d;
}



