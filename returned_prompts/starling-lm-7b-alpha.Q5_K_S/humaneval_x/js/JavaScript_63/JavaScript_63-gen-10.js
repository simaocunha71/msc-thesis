  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    const fibs = [0, 0, 1];
    for (let i = 3; i <= n; i++) {
      fibs[i] = fibs[i - 1] + fibs[i - 2] + fibs[i - 3];
    }
    return fibs[n];
  }
}


