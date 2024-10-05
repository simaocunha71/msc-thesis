const willItFly = (q, w) => {
  if (q.length === 1) return q[0] <= w;
  if (q.length === 2) return q[0] === q[1] && q[0] <= w;
  const mid = q.length / 2;
  const left = q.slice(0, mid);
  const right = q.slice(mid);
  return willItFly(left, w) && willItFly(right, w);
}
