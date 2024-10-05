/*
  The above solution is correct but it's not efficient, because it uses a recursive approach, which will result in a lot of function calls, and that will take a lot of time for bigger numbers.
  To make the above solution more efficient we can use a dynamic programming approach, where we store the result of the previous calculation so we don't need to recalculate the same thing every time.
*/
const fibfib = (n) => {
  if (n < 3) return n
  const arr = [0, 0, 1]
  for (let i = 3; i <= n; i++) {
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
  }
  return arr[n]
}
