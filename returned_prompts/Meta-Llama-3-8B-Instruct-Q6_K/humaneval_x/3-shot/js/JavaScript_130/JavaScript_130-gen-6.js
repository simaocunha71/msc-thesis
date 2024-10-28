  if (n == 0) {
    return [1];
  }
  if (n == 1) {
    return [1, 3];
  }
  if (n == 2) {
    return [1, 3, 2];
  }
  let sequence = [1, 3, 2];
  for (let i = 3; i <= n; i++) {
    let sum = 0;
    for (let j = 0; j < i; j++) {
      if (j % 2 == 0) {
        sum += sequence[j];
      }
    }
    sequence.push(sum);
  }
  return sequence;
}
// or use memoization
const tri = (n) => {
  const memo = { 0: [1], 1: [1, 3], 2: [1, 3, 2] };
  for (let i = 3; i <= n; i++) {
    memo[i] = [1, 3, ...memo[i - 1].reduce((prev, current) => prev.concat([current + (i % 2 == 0 ? memo[i - 1][0] : 0)]), [])];
  }
  return memo[n];
}