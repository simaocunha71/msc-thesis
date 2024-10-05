/* Return a string containing space-delimited numbers starting from 0 upto n inclusive.
  >>> stringSequence(0)
  '0'
  >>> stringSequence(5)
  '0 1 2 3 4 5'
  */
const stringSequence = (n) => {
  let str = '';
  for (let i = 0; i <= n; i++) {
    str += i + ' ';
  }
  return str.trim();
}