  let result = '';
  while (x > 0) {
    result = (x % base).toString() + result;
    x = Math.floor(x / base);
  }
  return result;
}