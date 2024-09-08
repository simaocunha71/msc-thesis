  if (n > m) return -1;

  let sum = 0;
  let count = m - n + 1;
  for (let i = n; i <= m; i++) {
    sum += i;
  }

  let average = Math.round(sum / count);
  return "0b" + average.toString(2);
}



