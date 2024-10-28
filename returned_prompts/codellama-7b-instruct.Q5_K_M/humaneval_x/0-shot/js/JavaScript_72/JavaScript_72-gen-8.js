function willItFly(q, w) {
  if (q.length < 2) return false;
  let sum = 0;
  let balanced = true;
  for (let i = 0; i < q.length; i++) {
    sum += q[i];
    if (q[i] !== q[q.length - 1 - i]) balanced = false;
  }
  if (balanced && sum <= w) return true;
  return false;
}
