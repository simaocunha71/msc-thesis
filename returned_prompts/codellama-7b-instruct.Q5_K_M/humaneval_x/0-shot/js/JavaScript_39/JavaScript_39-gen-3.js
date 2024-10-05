  const primeFib = (n) => {
    if (n <= 1) return 1;
    if (n === 2) return 2;
    if (n === 3) return 3;

    let last = 1;
    let current = 1;
    let next = 2;
    for (let i = 0; i < n - 3; i++) {
      last = current;
      current = next;
      next = last + current;
    }
    return next;
  }

  const isPrime = (n) => {
