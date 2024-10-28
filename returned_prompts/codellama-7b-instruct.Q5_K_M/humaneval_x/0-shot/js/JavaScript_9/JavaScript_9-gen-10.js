const rollingMax = (numbers) => numbers.reduce(
  (acc, x) => [...acc, Math.max(acc[acc.length - 1], x)],
  []
);

