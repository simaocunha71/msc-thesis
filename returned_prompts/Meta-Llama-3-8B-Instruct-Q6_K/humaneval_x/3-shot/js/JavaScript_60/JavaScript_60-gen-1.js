  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}
// or
const sumToN = (n) => {
  return (n * (n + 1)) / 2;
}
// or
const sumToN = (n) => {
  return Array(n).fill().reduce((a, b, i) => a + (i + 1), 0);
}