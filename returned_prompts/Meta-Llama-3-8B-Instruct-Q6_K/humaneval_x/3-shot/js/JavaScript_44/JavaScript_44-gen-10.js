  let result = '', remainder = 0;

  while (x > 0) {
    remainder = x % base;
    if (remainder > 9) {
      result = String.fromCharCode(55 + remainder) + result;
    } else {
      result = remainder.toString() + result;
    }
    x = Math.floor(x / base);
  }

  return result;
}