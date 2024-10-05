const willItFly = (q, w) => {
  if (!q.every((v, i) => v === q[q.length - i - 1])) return false;
  return q.reduce((a, v) => a + v, 0) <= w;
};