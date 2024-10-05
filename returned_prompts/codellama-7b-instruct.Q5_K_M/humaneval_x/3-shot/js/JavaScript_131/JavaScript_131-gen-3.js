  var result = 1;
  var temp = n;

  while (temp > 0) {
    var digit = temp % 10;
    if (digit % 2 == 1) {
      result *= digit;
    }
    temp = Math.floor(temp / 10);
  }

  return result;
}



