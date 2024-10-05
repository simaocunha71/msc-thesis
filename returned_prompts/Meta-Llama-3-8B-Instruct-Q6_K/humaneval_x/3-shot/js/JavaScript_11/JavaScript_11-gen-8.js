  let result = '';
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    let bitA = a[i] === undefined ? '0' : a[i];
    let bitB = b[i] === undefined ? '0' : b[i];
    result += (bitA === bitB) ? '0' : '1';
  }
  return result;
}