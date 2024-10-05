const roundedAvg = (n, m) => {
  if (n > m) {
    return -1;
  }
  const avg = (n + m) / 2;
  const rounded = Math.round(avg);
  return (rounded >>> 0).toString(2);
};
