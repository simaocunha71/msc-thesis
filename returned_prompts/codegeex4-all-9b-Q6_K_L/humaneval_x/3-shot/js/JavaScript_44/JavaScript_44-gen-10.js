  var result = '';

  while (x > 0) {
    var remainder = x % base;
    x = Math.floor(x / base);
    result = remainder + result;
  }

  return result;
}



