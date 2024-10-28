

/*
 * Return the nth Fibonacci number.
 * n: the index of the Fibonacci number
 * return: the nth Fibonacci number
 */
const fibfib = (n) => {
  const memo = [0, 0, 1];

  for (let i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];
  }

  return memo[n];
};

/*
 * 3rd solution: DP
 * O(n) time, O(n) space
 */
const fibfib = (n) => {
  const memo = [0, 0, 1];

  for (let i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];
  }

  return memo[n];
};

/*
 * 4th solution: O(n) time, O(1) space
 *
 */
const fibfib = (n) => {
  if (n <= 2) return n;

  let a = 0;
  let b = 1;
  let c = 1;

  for (let i = 3; i <= n; i++) {
    [a, b, c] = [b, c, a + b + c];
  }

  return c;
};

