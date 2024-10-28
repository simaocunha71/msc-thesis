  var result = 1;
  var n1 = n;
  var n2 = n - 1;

  while (n1 > 0) {
    for (var i = 1; i <= n1; i++) {
      result *= i;
    }
    n1 -= 1;
  }

  return result;
}



