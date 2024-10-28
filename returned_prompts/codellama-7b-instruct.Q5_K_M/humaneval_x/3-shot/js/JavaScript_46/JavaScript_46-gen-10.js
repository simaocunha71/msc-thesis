  var a = 0, b = 0, c = 2;
  for (let i = 0; i < n; i++) {
    a = b;
    b = c;
    c = a + b + c;
  }
  return c;
}



