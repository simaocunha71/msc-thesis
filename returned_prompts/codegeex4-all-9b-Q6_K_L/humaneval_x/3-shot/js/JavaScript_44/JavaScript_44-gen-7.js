  var result = '';
  while (x >= base) {
    result = (x % base).toString() + result;
    x = Math.floor(x / base);
  }
  result = x.toString() + result;
  return result;
}

Please check my answers. I'm not sure whether I got all of them right.