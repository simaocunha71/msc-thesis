  let collatz = [n];
  while (n != 1) {
    n = n % 2 === 0 ? n / 2 : n * 3 + 1;
    if (n % 2 !== 0) {
      collatz.push(n);
    }
  }
  return collatz.sort((a, b) => a - b);
}



