  let result = [];

  for (var i = 0; i < a.length; i++) {
    if (a[i] != b[i]) {
      result.push('1');
    } else {
      result.push('0');
    }
  }

  return result.join('');
}



