const stringXor = (a, b) => {
  let res = '';
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      res += '1';
    } else {
      res += '0';
    }
  }
  return res;
};

