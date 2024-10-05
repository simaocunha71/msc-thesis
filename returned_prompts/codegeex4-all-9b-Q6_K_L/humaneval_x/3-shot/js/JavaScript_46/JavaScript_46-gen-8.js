  if (n < 4) {
    return [0, 0, 2, 0][n];
  }

  var f = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    f.push(f[i-1] + f[i-2] + f[i-3] + f[i-4]);
  }
  return f[n];
}