  let collatz = [];
  while (n != 1) {
    if (n % 2 != 0) {
      collatz.push(n);
    }
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
  }
  collatz.push(1);
  return collatz.sort((a, b) => a - b);
}



