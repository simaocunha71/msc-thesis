const f = (n) => {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(i * factorial(i - 1));
    } else {
      result.push(sum(i));
    }
  }
  return result;
};

