  let result = '';
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      result += a[i];
    } else {
      result += '0';
    }
  }
  return result;
}