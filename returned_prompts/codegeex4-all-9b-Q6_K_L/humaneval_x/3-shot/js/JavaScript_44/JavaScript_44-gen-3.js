  var result = '';
  while (x > 0) {
    result = (x % base) + result;
    x = Math.floor(x / base);
  }
  return result;
}



