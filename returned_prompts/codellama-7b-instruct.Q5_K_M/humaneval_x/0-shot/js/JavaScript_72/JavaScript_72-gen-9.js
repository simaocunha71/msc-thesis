const willItFly = (q, w) => {
  if (q.every((v, i) => v === q[q.length - 1 - i])) {
    return q.reduce((a, c) => a + c, 0) <= w;
  }
  return false;
};
