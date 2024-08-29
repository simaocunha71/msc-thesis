  if (n <= 2) {
    return 0;
  }
  if (n == 3) {
    return 1;
  }

  const fibs = [0, 0, 1];
  while (fibs.length <= n) {
    fibs.push(fibs[fibs.length - 1] + fibs[fibs.length - 2] + fibs[fibs.length - 3]);
  }
  return fibs[fibs.length - 1];
}



