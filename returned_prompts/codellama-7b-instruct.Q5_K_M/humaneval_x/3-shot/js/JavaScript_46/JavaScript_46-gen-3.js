  var a = 0;
  var b = 0;
  var c = 2;
  var d = 0;

  while (n > 0) {
    var temp = a;
    a = b;
    b = c;
    c = d;
    d = temp + b + c + d;
    n--;
  }

  return d;
}



