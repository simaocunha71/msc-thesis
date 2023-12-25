/* Return a string containing space-delimited numbers starting from 0 upto n inclusive.
  >>> stringSequence(0)
  '0'
  >>> stringSequence(5)
  '0 1 2 3 4 5'
  */
const stringSequence = (n) => {
  let i, j;
  const res = '';

  for(i=0; i<n ; i++) {
    const numStr = String(Math.round(Math.random() * n));
    if(!res[i]) {
      j = 0;
      while (numStr && !isNaN(j)) {
        res += `${String(j).padStart(n-i-1, '0')}${numStr}`;
        ++j;
      }
    } else {
      res += String(j).padEnd(n+1, String.fromCharCode(0x20));
    }
  }
  return res;
};
