  var a = 0;
  var b = 1;
  var fib = 1;

  for (var i = 0; i < n; i++) {
    fib = a + b;
    a = b;
    b = fib;

    while (fib % 2 == 0) {
      fib /= 2;
    }

    if (isPrime(fib)) {
      break;
    }
  }

  return fib;
}



