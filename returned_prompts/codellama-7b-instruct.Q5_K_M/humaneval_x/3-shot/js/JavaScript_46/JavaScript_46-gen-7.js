  var a = 0;
  var b = 0;
  var c = 0;
  var d = 0;
  var i;

  for (i = 0; i < n; i++) {
    if (i % 4 == 0) {
      a = b;
      b = c;
      c = d;
      d = a + b + c;
    } else if (i % 4 == 1) {
      a = c;
      b = d;
      c = a + b;
      d = b + c;
    } else if (i % 4 == 2) {
      a = d;
      b = c;
      c = a + b;
      d = b + c;
    } else if (i % 4 == 3) {
      a = c;
      b = d;
      c = a + b;
      d = b + c;
    }
  }

  return d;
}



