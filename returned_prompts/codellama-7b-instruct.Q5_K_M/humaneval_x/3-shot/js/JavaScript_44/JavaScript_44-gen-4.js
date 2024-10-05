  var result = '';

  while (x > 0) {
    var remainder = x % base;
    result = String(remainder) + result;
    x = Math.floor(x / base);
  }

  return result;
}



