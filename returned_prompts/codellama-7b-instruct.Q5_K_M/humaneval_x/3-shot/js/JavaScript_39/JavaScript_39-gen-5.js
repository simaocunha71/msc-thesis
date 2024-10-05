  var a = 1;
  var b = 0;

  for (var i = 0; i < n; i++) {
    var c = a + b;
    var d = Math.floor(Math.sqrt(c));
    a = b;
    b = c;
    for (var j = 2; j <= d; j++) {
      if (c % j == 0) {
        c = a + b;
        a = b;
        b = c;
        i -= 1;
        break;
      }
    }
  }
  return c;
}



