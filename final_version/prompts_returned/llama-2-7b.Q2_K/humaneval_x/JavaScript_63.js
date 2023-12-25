/*The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
  fibfib(0) == 0
  fibfib(1) == 0
  fibfib(2) == 1
  fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
  Please write a function to efficiently compute the n-th element of the fibfib number sequence.
  >>> fibfib(1)
  0
  >>> fibfib(5)
  4
  >>> fibfib(8)
  24
  */
const fibfib = (n) => {
  let memo = [0, 0];
  let result;
  for (let i = 1; i <= n; i += 1) {
    const next = parseInt(memo[1]) + parseInt(memo[2]);
    if (i === 1 || i === 4) {
      memo = [next, next];
    } else {
      result = next;
    }
  }
  return result;
};
fibfib(8); // 24