  const isBalanced = JSON.stringify(q) === JSON.stringify(q.reverse());
  const sum = q.reduce((a, b) => a + b, 0);
  return isBalanced && sum <= w;
}