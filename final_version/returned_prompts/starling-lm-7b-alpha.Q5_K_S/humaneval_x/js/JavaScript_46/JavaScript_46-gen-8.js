  if (n < 4) {
    return 0;
  }
  const a = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    a[i] = a[i - 1] + a[i - 2] + a[i - 3] + a[i - 4];
  }
  return a[n];
}



