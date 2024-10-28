const stringXor = (a, b) => {
  let result = '';
  for (let i = 0; i < a.length; i++) {
    result += (a[i] === b[i] ? '0' : '1');
  }
  return result;
}
