  var collatz = [n];
  while (n != 1) {
    if (n % 2 == 1) {
      collatz.push(n);
    }
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }
  }
  return collatz.sort();
}