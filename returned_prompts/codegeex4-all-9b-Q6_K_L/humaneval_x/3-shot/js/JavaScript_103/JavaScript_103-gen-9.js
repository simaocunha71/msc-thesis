  if (n > m) {
    return -1;
  }

  let total = 0;
  for (let i = n; i <= m; i++) {
    total += i;
  }

  let avg = Math.round(total / (m - n + 1));
  return "0b" + avg.toString(2);
}