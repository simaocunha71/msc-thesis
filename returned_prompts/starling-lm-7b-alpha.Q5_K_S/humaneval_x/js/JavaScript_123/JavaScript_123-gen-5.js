  let result = [];
  const collatz = (n) => {
    if (n % 2 == 0) {
      return [n, n / 2];
    } else {
      return [n, 3 * n + 1];
    }
  };

  while (n != 1) {
    if (n % 2 == 1) {
      result.push(n);
    }
    [n, n] = collatz(n);
  }

  return result.sort((a, b) => a - b);
}



