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
  if (typeof n !== 'number') throw new TypeError('[modulo] First argument must be a number'); // eslint-disable-line no-invalid-this

  let temp;
  do {
    temp = Math.floor(Math.pow(2, n));
    if (n > 1) {
      if (!isPrime(temp)) {
        throw new RangeError('[modulo] First argument must be a prime number'); // eslint-disable-line no-invalid-this
      } else temp /= 2;
    }
  } while (n--); // eslint-disable-line no-loop-func, no-control-regex

  if (!isPrime(temp)) return -1; // eslint-disable-line no-invalid-this

  let ret = temp % p;
  if (ret < 0) {
    throw new RangeError('[modulo] Return value must be positive'); // eslint-disable-line no-invalid-this
    return modp(n + 1, p);
  } else return ret;
};

/**
  Return the greatest prime factor of n (useful for [pow() modulo p]).
   >>> pow10(30)
    5
*/
const pow10 = x => Math.round((Math.log(x + (x < 0))) / Math.LN10); // eslint-disable-line no-invalid-this, no-control-regex
/**
  Calculate n! modulo p with the Fermat method. N is limited to the int32 type range since it can't be greater than 2^53 - 1 (useful for [pow() modulo p]).
   >>>