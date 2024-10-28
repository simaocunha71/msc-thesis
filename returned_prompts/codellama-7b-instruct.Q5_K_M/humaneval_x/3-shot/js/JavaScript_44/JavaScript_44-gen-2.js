  let result = '';
  let digits = '0123456789ABCDEF';

  while (x > 0) {
    let remainder = x % base;
    result = digits[remainder] + result;
    x = Math.floor(x / base);
  }

  return result;
}



