  if (base > 10 || x < 0) {
    throw new Error('invalid input');
  }

  const digits = '0123456789ABCDEF'.split('');
  let result = '';

  while (x > 0) {
    const digit = x % base;
    result = digits[digit] + result;
    x = Math.floor(x / base);
  }

  return result;
}



