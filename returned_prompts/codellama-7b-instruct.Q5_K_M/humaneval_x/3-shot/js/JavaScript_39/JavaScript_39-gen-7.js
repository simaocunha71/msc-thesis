  var a = 0;
  var b = 1;

  for (var i = 0; i < n; i++) {
    var temp = a;
    a = b;
    b = temp + b;

    while (b % a == 0) {
      b = b / a;
    }
  }

  return b;
}



