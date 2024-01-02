/*sumToN is a function that sums numbers from 1 to n.
  >>> sumToN(30)
  465
  >>> sumToN(100)
  5050
  >>> sumToN(5)
  15
  >>> sumToN(10)
  55
  >>> sumToN(1)
  1
  */
const sumToN = (n) => {
  let i;
  const result = 0;
  if (!Number.isInteger(n)) throw new RangeError('sumToN, n is not an integer')
  for (i = 1; i <= n; ++i) {
    result += i;
  }
  return result;
}