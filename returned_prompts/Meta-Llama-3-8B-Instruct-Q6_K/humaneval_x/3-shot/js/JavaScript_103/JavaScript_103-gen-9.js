  if (n > m) {
    return -1;
  }
  let sum = 0;
  for (let i = n; i <= m; i++) {
    sum += i;
  }
  let average = Math.round(sum / (m - n + 1));
  return average.toString(2);
}