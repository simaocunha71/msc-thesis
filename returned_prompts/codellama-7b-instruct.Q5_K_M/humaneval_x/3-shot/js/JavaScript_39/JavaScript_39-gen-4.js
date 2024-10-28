  var a = 0, b = 1;
  for (var i = 0; i < n; i++) {
    var c = a + b;
    if (isPrime(c)) {
      return c;
    }
    a = b;
    b = c;
  }
}



