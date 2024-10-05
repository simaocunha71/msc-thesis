  var a = 0;
  var b = 0;
  var c = 2;

  for (var i = 0; i < n; i++) {
    var d = a + b + c;
    a = b;
    b = c;
    c = d;
  }

  return c;
}



