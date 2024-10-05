  var a = 1;
  var b = 2;
  for (var i = 0; i < n - 1; i++) {
    var c = a + b;
    a = b;
    b = c;
    if (isPrime(a)) {
      return a;
    }
  }
  return b;
}



