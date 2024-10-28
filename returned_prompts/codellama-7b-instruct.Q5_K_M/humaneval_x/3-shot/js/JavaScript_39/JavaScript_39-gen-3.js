  var a = 0;
  var b = 1;
  var i = 1;

  while (i < n) {
    var c = a + b;
    a = b;
    b = c;
    i += 1;
  }

  while (!isPrime(b)) {
    var c = a + b;
    a = b;
    b = c;
  }

  return b;
}



