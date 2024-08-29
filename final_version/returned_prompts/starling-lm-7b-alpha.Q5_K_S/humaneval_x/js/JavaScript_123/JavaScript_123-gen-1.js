  const collatz = [];
  let current = n;

  while (current != 1) {
    if (current % 2 == 0) {
      current = current / 2;
    } else {
      current = 3 * current + 1;
      collatz.push(current);
    }
  }

  return collatz.sort((a, b) => a - b);
}



