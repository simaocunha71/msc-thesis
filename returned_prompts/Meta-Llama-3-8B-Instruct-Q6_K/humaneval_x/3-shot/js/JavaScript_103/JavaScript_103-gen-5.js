  if (n > m) {
    return -1;
  }
  const sum = Math.floor((m - n + 1) / 2) * (n + m);
  const avg = sum / (m - n + 1);
  const rounded = Math.round(avg);
  return rounded.toString(2);
}