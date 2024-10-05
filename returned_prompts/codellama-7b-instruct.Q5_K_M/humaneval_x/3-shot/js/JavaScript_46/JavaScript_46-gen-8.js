  var a = 0;
  var b = 0;
  var c = 2;
  var d = 0;

  while (n >= 0) {
    d = c;
    c = b;
    b = a;
    a = d + c + b;
    n -= 1;
  }

  return a;
}



