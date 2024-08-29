  let result = [];

  function collatz(n) {
    if (n % 2 == 0) {
      return [n / 2];
    } else {
      return [3 * n + 1, ...collatz(3 * n + 1)];
    }
  }

  let collatz_sequence = collatz(n);

  for (let i = 0; i < collatz_sequence.length; i++) {
    if (collatz_sequence[i] % 2 === 1) {
      result.push(collatz_sequence[i]);
    }
  }

  return result;
}



