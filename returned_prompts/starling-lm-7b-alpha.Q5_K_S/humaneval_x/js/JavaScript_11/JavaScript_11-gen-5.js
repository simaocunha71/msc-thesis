  let result = '';
  for (let i = 0; i < a.length; i++) {
    if (a[i] == '1' && b[i] == '1') {
      result += '0';
    } else {
      result += '1';
    }
  }
  return result;
}



