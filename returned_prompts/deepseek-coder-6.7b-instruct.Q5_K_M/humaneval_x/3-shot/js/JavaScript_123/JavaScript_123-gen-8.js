  let collatz = [n];
  while (n != 1) {
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }
    collatz.push(n);
  }
  return collatz.filter(n => n % 2 != 0).sort((a, b) => a - b);
}



