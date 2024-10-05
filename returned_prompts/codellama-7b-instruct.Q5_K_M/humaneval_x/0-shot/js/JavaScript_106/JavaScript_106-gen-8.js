const f = (n) => {
  const res = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      res.push(i * i * i);
    } else {
      res.push(res.reduce((a, b) => a + b));
    }
  }
  return res;
};