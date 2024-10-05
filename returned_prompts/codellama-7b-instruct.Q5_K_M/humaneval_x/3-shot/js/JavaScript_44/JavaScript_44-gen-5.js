  var result = [];
  var digits = '0123456789ABCDEF';

  while (x > 0) {
    result.unshift(digits[x % base]);
    x = Math.floor(x / base);
  }

  return result.join('');
}



