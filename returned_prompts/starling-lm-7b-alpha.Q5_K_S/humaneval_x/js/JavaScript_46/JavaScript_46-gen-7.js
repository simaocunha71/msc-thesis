  if (n == 0 || n == 1) return 0;
  if (n == 2) return 2;
  if (n == 3) return 0;

  var fibs = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    fibs[i] = fibs[i - 1] + fibs[i - 2] + fibs[i - 3] + fibs[i - 4];
  }

  return fibs[n];
}



