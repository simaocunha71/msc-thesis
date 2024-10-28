  if (n > m) {
    return -1;
  }

  let sum = 0;
  for (let i = n; i <= m; i++) {
    sum += i;
  }

  let avg = sum / (m - n + 1);
  let rounded_avg = Math.round(avg);

  return rounded_avg.toString(2);
}



