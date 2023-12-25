/* Input are two strings a and b consisting only of 1s and 0s.
  Perform binary XOR on these inputs and return result also as a string.
  >>> stringXor('010', '110')
  '100'
  */
const stringXor = (a, b) => {
  let c = '';
  for (let i = 0; i < a.length + b.length - 1; i++) {
    if ((i < a.length && i < b.length && (parseInt(a[i]) ^ parseInt(b[i]))) ||
      (i >= a.length && i >= b.length && (parseInt(a[i - 1]) ^ parseInt(b[i - 1])))) {
      c += a[i];
    } else {
      c += a[i];
    }
  }
  return c;
};
