  var collatz = [];
  while (n > 1) {
    if (n % 2 == 1) {
      collatz.push(n);
    }
    n = Math.floor(n / 2);
  }
  collatz.push(1);
  return collatz.sort((a, b) => a - b);
}