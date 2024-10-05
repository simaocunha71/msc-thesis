  var result = [];
  var carry = 0;

  for (var i = 0; i < a.length; i++) {
    if (a[i] == '1' && b[i] == '1') {
      result.push('0');
      carry = 1;
    } else if (a[i] == '0' && b[i] == '0') {
      result.push('0');
      carry = 0;
    } else if (a[i] == '0' && b[i] == '1') {
      result.push('1');
      carry = 1;
    } else if (a[i] == '1' && b[i] == '0') {
      result.push('1');
      carry = 0;
    }
  }

  if (carry == 1) {
    result.push('1');
  }

  return result.join('');
}



