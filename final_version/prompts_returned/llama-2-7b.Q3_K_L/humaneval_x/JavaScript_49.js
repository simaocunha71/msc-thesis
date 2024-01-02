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
  if (typeof n !== 'number') throw new TypeError('expecting numeric value');
  const pow = p.toString().length * 3;
  if (pow < 2) return Number(n % p);
  let temp = Math.abs((n % p)).toFixed(12);
  while (temp >= p) {
    n += p;
    temp /= p;
  }
  return Math.abs(n - modp(Math.floor(n), p));
};
