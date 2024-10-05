  let collatz = [n];

  while (n != 1) {
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
    if (n % 2 !== 0) {
      collatz.push(n);
    }
  }

  return collatz.sort((a, b) => a - b);
}



