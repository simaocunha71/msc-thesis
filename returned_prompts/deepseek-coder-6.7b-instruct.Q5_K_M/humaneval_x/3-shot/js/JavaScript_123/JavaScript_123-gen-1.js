  var collatz = [n];
  while (n != 1) {
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = n * 3 + 1;
    }
    if (n % 2 != 0) {
      collatz.push(n);
    }
  }
  return collatz.sort((a, b) => a - b);
}



