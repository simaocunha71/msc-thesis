  let collatz = [n];
  while (n != 1) {
    if (n % 2 != 0) {
      collatz.push(n);
    }
    n = n % 2 ? n*3 + 1 : n / 2;
  }
  return collatz.sort((a, b) => a - b);
}



