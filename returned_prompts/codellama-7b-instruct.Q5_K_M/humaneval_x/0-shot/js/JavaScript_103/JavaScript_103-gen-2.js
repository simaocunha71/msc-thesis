const roundedAvg = (n, m) => {
  if (n > m) return -1;
  const avg = ((n + m) / 2).toFixed(0);
  return (avg >> 0).toString(2);
};

