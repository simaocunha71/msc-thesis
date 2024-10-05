  var result = [];
  var unique_digits = [];

  for (var i = 0; i < x.length; i++) {
    var digit = 1;
    while (x[i] >= digit) {
      digit *= 10;
    }
    unique_digits.push(digit);
  }

  for (var i = 0; i < x.length; i++) {
    for (var j = 0; j < unique_digits.length; j++) {
      if (x[i] % unique_digits[j] == 0) {
        result.push(x[i]);
      }
    }
  }

  return result;
}



