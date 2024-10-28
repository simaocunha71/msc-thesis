  if (n > m) {
    return -1;
  }
  const sum = Array.from({length: m - n + 1}, (_, i) => n + i).reduce((a, b) => a + b, 0);
  const avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
}