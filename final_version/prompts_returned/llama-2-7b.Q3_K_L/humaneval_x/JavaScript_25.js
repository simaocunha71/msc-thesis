/* Return list of prime factors of given integer in the order from smallest to largest.
  Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
  Input number should be equal to the product of all factors
  >>> factorize(8)
  [2, 2, 2]
  >>> factorize(25)
  [5, 5]
  >>> factorize(70)
  [2, 5, 7]
  */
const factorize = (n) => {
  let arr = [];
  for (let i = n; ; i--) {
    if (!((i % 1 === 0))) break;
    arr.push(Math.floor(i / Math.sqrt(i)));
  }
  return arr;
};
