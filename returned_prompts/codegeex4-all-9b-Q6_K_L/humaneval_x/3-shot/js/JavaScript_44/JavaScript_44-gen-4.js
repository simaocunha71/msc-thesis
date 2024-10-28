  var result = '';
  var temp = x;

  while (temp > 0) {
    result = (temp % base) + result;
    temp = Math.floor(temp / base);
  }

  return result;
}



