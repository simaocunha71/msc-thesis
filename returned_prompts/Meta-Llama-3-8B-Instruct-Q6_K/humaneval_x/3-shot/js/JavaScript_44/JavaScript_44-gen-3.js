  let result = '';
  while (x > 0) {
    result = String(x % base) + result;
    x = Math.floor(x / base);
  }
  return result;
}...



