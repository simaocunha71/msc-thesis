  if (n <= 1) {
    return n;
  } else {
    let a = 0;
    let b = 1;
    for (let i = 2; i <= n; i++) {
      let temp = a;
      a = b;
      b = temp + b;
    }
    return b;
  }
}
// or using recursion
const fib = (n) => {
  if (n <= 1) {
    return n;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}
// or using memoization
const memo = {};
const fib = (n) => {
  if (n <= 1) {
    return n;
  } else if (memo[n]) {
    return memo[n];
  } else {
    memo[n] = fib(n - 1) + fib(n - 2);
    return memo[n];
  }
}
// or using dynamic programming
const fib = (n) => {
  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
}
// or using matrix exponentiation
const fib = (n) => {
  const F = [[1, 1], [1, 0]];
  if (n == 0) return 0;
  const M = matrixPower(F, n - 1);
  return M[0][0];
}

function matrixPower(M, n) {
  if (n == 1) return M;
  const half = matrixPower(M, Math.floor(n / 2));
  if (n % 2 == 0) return matrixMultiply(half, half);
  return matrixMultiply(matrixMultiply(half, half), M);

  function matrixMultiply(A, B) {
    const C = [[0, 0], [0, 0]];
    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < 2; j++) {
        for (let k = 0; k < 2; k++) {
          C[i][j] += A[i][k] * B[k][j];
        }
      }
    }
    return C;
