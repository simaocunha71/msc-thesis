
const stringXor = (a, b) => {
  let result = '';
  for (let i = 0; i < a.length; i++) {
    result += String(Number(a[i]) ^ Number(b[i]));
  }
  return result;
};
