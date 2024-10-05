const roundedAvg = (n, m) => {
  const avg = (n + m) / 2;
  if (n > m) return -1;
  return avg.toFixed(0).toString(2);
};
