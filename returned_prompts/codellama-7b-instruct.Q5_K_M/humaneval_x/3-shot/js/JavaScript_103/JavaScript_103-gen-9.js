  if (n > m) {
    return -1;
  }
  const sum = (n + m) * (m - n + 1) / 2;
  const avg = sum / 2;
  const rounded_avg = Math.round(avg);
  return rounded_avg.toString(2);
}



