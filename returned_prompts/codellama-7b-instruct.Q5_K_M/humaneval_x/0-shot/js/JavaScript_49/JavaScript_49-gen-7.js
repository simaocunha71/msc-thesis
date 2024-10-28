/*Return 2^n modulo p (be aware of numerics).
  >>> modp(3, 5)
  3
  >>> modp(1101, 101)
  2
  >>> modp(0, 101)
  1
  >>> modp(3, 11)
  8
  >>> modp(100, 101)
  1
  */
const modp = (n, p) => {
  const result = 2 ** n % p
  return result === 0 ? p - 1 : result
}

B:
/*Return 2^n modulo p (be aware of numerics).
  >>> modp(3, 5)
  3
  >>> modp(1101, 101)
  2
  >>> modp(0, 101)
  1
  >>> modp(3, 11)
  8
  >>> modp(100, 101)
  1
  */
const modp = (n, p) => (2 ** n) % p

C:
/*Return 2^n modulo p (be aware of numerics).
  >>> modp(3, 5)
  3
  >>> modp(1101, 101)
  2
  >>> modp(0, 101)
  1
  >>> modp(3, 11)
  8
  >>> modp(100, 101)
  1
  */
const modp = (n, p) => Math.pow(2, n) % p

D:
/*Return 2^n modulo p (be aware of numerics).
  >>> modp(3, 5)
  3
  >>> modp(1101, 101)
  2
  >>> modp(0, 101)
  1
  >>> modp(3, 11)
  8
  >>> modp(100, 101)
  1
  */
const modp = (n, p) => {
  const