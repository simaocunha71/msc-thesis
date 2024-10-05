const median = (l) => {
  l.sort();
  const n = l.length;
  if (n % 2 === 0) {
    return (l[n / 2 - 1] + l[n / 2]) / 2;
  }
  return l[n / 2 | 0];
};
