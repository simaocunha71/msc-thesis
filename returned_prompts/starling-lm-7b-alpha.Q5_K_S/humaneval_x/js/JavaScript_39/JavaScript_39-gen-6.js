  var fibs = [2, 3];
  for (var i = 3; i <= n; i++) {
    var fib = fibs[i-1] + fibs[i-2];
    while (!isPrime(fib)) {
      fib += fibs[i-1];
    }
    fibs.push(fib);
  }
  return fibs[n];
}



