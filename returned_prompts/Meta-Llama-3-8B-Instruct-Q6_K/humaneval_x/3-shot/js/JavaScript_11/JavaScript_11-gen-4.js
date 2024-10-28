  let result = '';
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    let bitA = a[i] || '0';
    let bitB = b[i] || '0';
    result += (bitA ^ bitB).toString();
  }
  return result;
}
