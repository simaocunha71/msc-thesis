  let result = '';
  let remainder;

  while (x > 0) {
    remainder = x % base;
    if (remainder >= 10) {
      remainder = String.fromCharCode(55 + remainder - 10);
    }
    result = remainder + result;
    x = Math.floor(x / base);
  }

  return result;
}