  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}
// Alternative
const sumToN = (n) => {
  return n * (n + 1) / 2;
}
// This is a more efficient way to calculate the sum of numbers from 1 to n. It uses the formula for the sum of an arithmetic series.