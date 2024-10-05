  var a = 0;
  var b = 1;
  var c = 0;
  var d = 1;

  for (let i = 0; i < n - 2; i++) {
    a = b;
    b = c;
    c = d;
    d = a + b + c;
  }

  return d;
}



