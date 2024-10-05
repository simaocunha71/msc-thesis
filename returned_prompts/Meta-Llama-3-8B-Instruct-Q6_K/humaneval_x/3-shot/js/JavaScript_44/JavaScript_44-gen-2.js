  let result = '';
  while (x > 0) {
    let remainder = x % base;
    if (remainder < 10) {
      result = remainder.toString() + result;
    } else {
      result = String.fromCharCode(55 + remainder) + result;
    }
    x = Math.floor(x / base);
  }
  return result;
}