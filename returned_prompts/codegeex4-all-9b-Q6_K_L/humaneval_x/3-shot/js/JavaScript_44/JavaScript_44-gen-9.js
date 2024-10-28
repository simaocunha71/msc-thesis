  var result = '';
  while (x > 0) {
    var remainder = x % base;
    result = remainder.toString() + result;
    x = Math.floor(x / base);
  }
  return result;
}

