  const fibs = [0, 0, 2];

  for (let i = 3; i <= n; i++) {
    fibs[i] = fibs[i - 1] + fibs[i - 2] + fibs[i - 3];
  }

  return fibs[n];
};



