  let sum = 0;
  let balanced = true;
  for (let i = 0; i < q.length; i++) {
    sum += q[i];
    if (q[i] !== q[q.length - 1 - i]) {
      balanced = false;
    }
  }
  return balanced && sum <= w;
}